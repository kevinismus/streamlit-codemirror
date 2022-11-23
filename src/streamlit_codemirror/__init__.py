from pathlib import Path
from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called streamlit_codemirror,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
	"st_codemirror", path=str(frontend_dir)
)

# Create the python function that will be called
def st_codemirror(
    text: Optional[str],
    key: Optional[str] = None,
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        text=text,
        key=key,
    )

    return component_value


def main():
    st.write("## Example")
    value = st_codemirror(
        text="SELECT * FROM table"
    )

    st.write(value)


if __name__ == "__main__":
    main()
