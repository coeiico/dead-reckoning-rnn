"""
The model for dead-reckoning-rnn.

an RNN (vanilla or LSTM, 256–1024 units). Input is velocity (speed, plus heading as
sine and cosine). Output is a population code over simulated place cells in the arena,
which works better than predicting raw (x, y).

forward() accepts return_cache=True and returns a dict of internal activations, and a
patch argument (or forward hooks) overwrites a named activation for interventions.
"""

# TODO: implement. See README.md for the plan.
