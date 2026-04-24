import numpy as np

class ErgodicityEngine:
    def __init__(self, n_agents, n_steps, edge, volatility, reset_threshold):
        self.n_agents = n_agents
        self.n_steps = n_steps
        self.edge = edge
        self.volatility = volatility
        self.reset_threshold = reset_threshold

    def calculate_kelly(self):
        """Calculates the optimal bet fraction."""
        # Simple Kelly: f = mu / sigma^2
        if self.volatility == 0: return 1.0
        f = self.edge / (self.volatility**2)
        return np.clip(f, 0.0, 1.0)

    def run(self, use_kelly=True):
        wealth = np.ones((self.n_steps, self.n_agents))
        f = self.calculate_kelly() if use_kelly else 1.0
        
        for t in range(1, self.n_steps):
            # Geometric Brownian Motion simulation
            shocks = np.random.normal(self.edge, self.volatility, self.n_agents)
            wealth[t] = wealth[t-1] * (1 + (f * shocks))
            
            # Reset Mechanism (Insurance/Safety Net)
            wealth[t] = np.where(wealth[t] < self.reset_threshold, 1.0, wealth[t])
            
        return wealth, f