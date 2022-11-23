# streamlit-codemirror

A streamlit component that adds a CodeMirror instance into your Streamlit dashboard

## Installation instructions 

```sh
pip install streamlit-codemirror
```

## Usage instructions

```python
import streamlit as st

from streamlit_codemirror import streamlit_codemirror

value = streamlit_codemirror()

st.write(value)
