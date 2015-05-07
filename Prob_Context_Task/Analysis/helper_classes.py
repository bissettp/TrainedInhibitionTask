# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:09:29 2015

@author: Ian
"""

import random as r
import numpy as np
from scipy.stats import norm
from helper_functions import softmax 

class PredModel:
    """
    Prediction model that takes in data, and uses a prior over hypotheses
    and the relevant to calculate posterior hypothesis estimates.
    """
    def __init__(self, likelihood_dist, prior, recursive_prob = .9,
                 data_noise = 0, mode = "optimal"):
        self.prior = prior
        self.likelihood_dist = likelihood_dist
        self.recursive_prob = recursive_prob
        self.mode = mode
        self.posterior = prior
        
    def calc_posterior(self, data, noise = 0):
        """
        Calculate the posterior probability of different distribution hypotheses
        given the data. You can set a noise value which will set add gaussian
        noise to the observation. The value specified will be a scaling parameter. 
        It should always be less than one. 
        """
        ld = self.likelihood_dist
        rp = self.recursive_prob
        prior = self.prior
        mode = self.mode

        if noise:
            data= min(max(data + noise*norm().rvs(),-1),1)
                                   
        trans_probs = np.array([[rp, 1-rp], [1-rp, rp]])    
                     
        n = len(prior)
        likelihood = [dis.pdf(data) for dis in ld]
        numer = np.array([likelihood[i] * prior[i] for i in range(n)])
        try:
            dinom = [np.sum(zip(*numer)[i]) for i in range(len(numer[0]))]
        except TypeError:
            dinom = np.sum(numer)
        posterior = numer/dinom
        
        if mode == "single":
            self.prior = trans_probs[np.argmax(posterior),:]
        elif mode == 'optimal':
            self.prior = np.dot(trans_probs,posterior)
        self.posterior = posterior
        return posterior
        
    def set_mode(self, mode):
        self.mode = mode
        
    def choose(self, mode = 'softmax', eps = .1, inv_temp = 1):
        if mode == "e-greedy":
            if r.random() < eps:
                return r.randint(0,2)
            else:
                return np.argmax(self.posterior)
        elif mode == "softmax":
            probs = softmax(self.posterior, inv_temp)
            return np.random.choice(range(len(probs)), p = probs)
        else:
            return np.argmax(self.posterior)
            
class BiasPredModel:
    """
    Prediction model that takes in data, and uses a prior over hypotheses
    and the relevant to calculate posterior hypothesis estimates.
    """
    def __init__(self, likelihood_dist, prior, recursive_prob = .9,
                 data_noise = 0, ts_bias = 0):
        self.prior = np.array(prior)
        self.likelihood_dist = likelihood_dist
        self.recursive_prob = recursive_prob
        self.ts_bias = ts_bias
        self.posterior = prior
        
    def calc_posterior(self, data, noise = 0):
        """
        Calculate the posterior probability of different distribution hypotheses
        given the data. You can set a noise value which will set add gaussian
        noise to the observation. The value specified will be a scaling parameter. 
        It should always be less than one. 
        """
        ld = self.likelihood_dist
        rp = self.recursive_prob
        prior = self.prior
        ts_bias = self.ts_bias
        prior[1]*=ts_bias
        prior = prior/sum(prior)

        if noise:
            data= min(max(data + noise*norm().rvs(),-1),1)
                                   
        trans_probs = np.array([[rp, 1-rp], [1-rp, rp]])    
                     
        n = len(prior)
        likelihood = np.array([dis.pdf(data) for dis in ld])
        numer = np.array([likelihood[i] * prior[i] for i in range(n)])
        try:
            dinom = [np.sum(zip(*numer)[i]) for i in range(len(numer[0]))]
        except TypeError:
            dinom = np.sum(numer)
        posterior = numer/dinom
        
        self.prior = np.dot(trans_probs,posterior)
        self.posterior = posterior
        return posterior
       
    def choose(self, mode = 'softmax', eps = .1, inv_temp = 1):
        if mode == "e-greedy":
            if r.random() < eps:
                return r.randint(0,2)
            else:
                return np.argmax(self.posterior)
        elif mode == "softmax":
            probs = softmax(self.posterior, inv_temp)
            return np.random.choice(range(len(probs)), p = probs)
        else:
            return np.argmax(self.posterior)

class EstimatePredModel:
    """
    Prediction model that takes in data, and uses a prior over hypotheses
    and the relevant to calculate posterior hypothesis estimates.
    """
    def __init__(self, prior, mean = 0, std = .37, recursive_prob = .9):
        self.prior = np.array(prior)
        self.likelihood_dist = [norm(mean, std),norm(-mean,std)]
        self.recursive_prob = recursive_prob
        self.posterior = prior
        
    def calc_posterior(self, data, noise = 0):
        """
        Calculate the posterior probability of different distribution hypotheses
        given the data. You can set a noise value which will set add gaussian
        noise to the observation. The value specified will be a scaling parameter. 
        It should always be less than one. 
        """
        ld = self.likelihood_dist
        rp = self.recursive_prob
        prior = self.prior

        if noise:
            data= min(max(data + noise*norm().rvs(),-1),1)
                                   
        trans_probs = np.array([[rp, 1-rp], [1-rp, rp]])    
                     
        n = len(prior)
        likelihood = np.array([dis.pdf(data) for dis in ld])
        numer = np.array([likelihood[i] * prior[i] for i in range(n)])
        try:
            dinom = [np.sum(zip(*numer)[i]) for i in range(len(numer[0]))]
        except TypeError:
            dinom = np.sum(numer)
        posterior = numer/dinom
        
        self.prior = np.dot(trans_probs,posterior)
        self.posterior = posterior
        return posterior
       
    def choose(self, mode = 'softmax', eps = .1, inv_temp = 1):
        if mode == "e-greedy":
            if r.random() < eps:
                return r.randint(0,2)
            else:
                return np.argmax(self.posterior)
        elif mode == "softmax":
            probs = softmax(self.posterior, inv_temp)
            return np.random.choice(range(len(probs)), p = probs)
        else:
            return np.argmax(self.posterior)
            
class DataGenerator:
    """
    creates generator for taskset data based on task-set distributions and
    transition probabilities (defined by recursive_p)
    """
    def __init__(self,ts_dis, recursive_p):
        self.ts_dis = ts_dis
        self.rp = recursive_p
        self.curr_ts = r.choice([0,1])
        self.ts_reps = 1
        self.stim_ids = [(0,2),(0,3),(1,2),(1,3)]
        self.trial_count = 0
        
        
    def gen_data(self):
        rp = self.rp
        ts = self.curr_ts
        dis = self.ts_dis[ts]
        trans_probs = np.array([[rp, 1-rp], [1-rp, rp]])
        bin_boundaries = np.linspace(-1,1,11)
        binned = -1.1 + np.digitize([dis.rvs()],bin_boundaries)*.2
        context_sample = max(-1, min(1, binned[0]))
        trial = {
                'trial_count': self.trial_count,
                'ts': ts,
                'c_dis': {'mean': dis.mean(), 'sd': dis.std()},
                'context': context_sample,
                'stim': r.choice(self.stim_ids)
            }
        if r.random() > trans_probs[ts,ts] or self.ts_reps >= 25:
            self.curr_ts = 1-ts
            self.ts_reps = 1
        else:
            self.ts_reps += 1
        self.trial_count += 1
        return trial
        
