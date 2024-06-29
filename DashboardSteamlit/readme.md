# Basic concepts of Streamlit

## Run:
  - `streamlit run your_script.py` optional `streamlit run your_script.py [-- script args]`
  - Is equivalent to: `python -m streamlit run your_script.py`

## Write a data frame:
  - `st.write("Text")`
  - Create a data frame and change its formatting with a Pandas _Styler_ object. 
  - Example:
    ``` Python
    import streamlit as st
    import pandas as pd

    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))
    ```

## Draw charts and maps:
  - Streamlit support several popular data charting libraries.

## Draw a line chart:
  - `st.line_chart(chart_data)` 
  - Example:
    ``` Python
    import streamlit as st
    import numpy as np
    import pandas as pd

    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
    ```

## Plot a map:
  - `st.map()`
  - Display data points on a map.
    - Example:
      ``` Python
      import streamlit as st
      import numpy as np
      import pandas as pd

      map_data = pd.DataFrame(
          np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
          columns=['lat', 'lon'])

      st.map(map_data)
      ```

## Widgets:
  - Treat widgets as variables:
    - `st.silder()`
      - Example:
        ``` Python
        import streamlit as st
        x = st.slider('x')  # 👈 this is a widget
        st.write(x, 'squared is', x * x)
        ```
    - `st.button()`
    - `st.selectbox()`
    - `st.text_input()`
      - Example:
        ``` Python
        import streamlit as st
        st.text_input("Your name", key="name")

        # You can access the value at any point with:
        st.session_state.name
        ```

## Use checkbox to show/hide data:
  - `st.checkbox()`
  - Takes a single argument, which is the widget label.
    - Example:
      ``` Python
      import streamlit as st
      import numpy as np
      import pandas as pd

      if st.checkbox('Show dataframe'):
          chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])

          chart_data
      ```

## Use a selectbox for options:
  - `st.selectbox()`
  - Use selectbox to choose from a series. You can write in the options you want, or pass through an array or data frame column.
    - Example
      ``` Python
      import streamlit as st
      import pandas as pd

      df = pd.DataFrame({
          'first column': [1, 2, 3, 4],
          'second column': [10, 20, 30, 40]
          })

      option = st.selectbox(
          'Which number do you like best?',
          df['first column'])

      'You selected: ', option
      ```

## Layout:
  - `st.sidebar`
  - Streamlit makes it easy to organize your widgets in a left panel sidebar with st.sidebar. Each element that's passed to st.sidebar is pinned to the left, allowing users to focus on the content in your app while still having access to UI controls.
    - Example:
      ``` Python
      import streamlit as st

      # Add a selectbox to the sidebar:
      add_selectbox = st.sidebar.selectbox(
          'How would you like to be contacted?',
          ('Email', 'Home phone', 'Mobile phone')
      )

      # Add a slider to the sidebar:
      add_slider = st.sidebar.slider(
          'Select a range of values',
          0.0, 100.0, (25.0, 75.0)
      )
      ```
  - Beyond the sidebar, Streamlit offers several other ways to control the layout of your app. st.columns lets you place widgets side-by-side, and st.expander lets you conserve space by hiding away large content.
  - Example:
    ``` Python
    import streamlit as st

    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.button('Press me!')

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")
    ```

## Show progress
- `st.progress()`
- When adding long running computations to an app, you can use st.progress() to display status in real time.
  - Example
    ```
    import streamlit as st
    import time

    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
      # Update the progress bar with each iteration.
      latest_iteration.text(f'Iteration {i+1}')
      bar.progress(i + 1)
      time.sleep(0.1)

    '...and now we\'re done!'
    ```