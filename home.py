import streamlit as st
import serial
from utils import receive_data
ser = serila.Serial('COM3' , 115200, timeout = 1)
st.write(receive_data())
