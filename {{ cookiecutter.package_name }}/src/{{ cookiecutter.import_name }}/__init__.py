from typing import Optional

import streamlit as st
import streamlit.components.v1 as components

# Tell streamlit that there is a component called {{ cookiecutter.import_name }},
# and that the code to display that component is in the "frontend" folder
_component_func = components.declare_component(
	"{{ cookiecutter.import_name }}", path="frontend")
)

# Create the python function that will be called
def {{ cookiecutter.import_name }}(
    key: Optional[str] = None,
):
    """
    Add a descriptive docstring
    """
    component_value = _component_func(
        key=key,
    )

    return component_value


def main():
    st.write("## Example")
    value = {{ cookiecutter.import_name }}()

    st.write(value)


if __name__ == "__main__":
    main()
