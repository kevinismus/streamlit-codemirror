# streamlit-codemirror

A streamlit component that adds a CodeMirror instance into your Streamlit dashboard. Currently only support SQL theme.

## Installation instructions 

```sh
pip install streamlit-codemirror
```

## Usage instructions

```python
import streamlit as st

from streamlit_codemirror import st_codemirror

value = st_codemirror()

st.write(value)
