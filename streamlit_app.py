import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler

# Load pre-trained models and scalers
# scaler = joblib.load('scaler.pkl')
pca_group1 = joblib.load('pca_group1.pkl')
