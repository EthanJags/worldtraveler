import streamlit as st
from datetime import datetime, timedelta

# Dictionary containing each country and its bordering countries
borders = {
    "USA": ["Canada", "Mexico"],
    "Canada": ["USA"],
    "Mexico": ["USA", "Guatemala", "Belize"],
    "Guatemala": ["Mexico", "Belize", "Honduras", "El Salvador"],
    "Belize": ["Mexico", "Guatemala"],
    "Honduras": ["Guatemala", "El Salvador", "Nicaragua"],
    "El Salvador": ["Guatemala", "Honduras"],
    "Nicaragua": ["Honduras", "Costa Rica"],
    "Costa Rica": ["Nicaragua", "Panama"],
    "Panama": ["Costa Rica", "Colombia"],
    # Add more countries and their borders here
}

# Start the game
# Title Card
st.title("World Traveler Game")
# Enter the starting country
# call a function to start the game when input entered
start_country = st.text_input("Enter the starting country:")
if st.button("Start Game"):
    if start_country in borders:
        current_country = start_country
        countries_visited = [start_country] # initialize the list of countries visited, starting with the first country
        country_count = 1
        mistakes = 0
        start_time = datetime.now()
        # call a function to process the next country when button clicked
        
    else:
        st.error("Invalid country. Please enter a valid country.")














# Initialize session state
if "current_country" not in st.session_state:
    st.session_state.current_country = None
if "countries_visited" not in st.session_state:
    st.session_state.countries_visited = []
if "mistakes" not in st.session_state:
    st.session_state.mistakes = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = datetime.now()
if "end_time" not in st.session_state:
    st.session_state.end_time = None

# Function to start the game
def start_game():
    start_country = st.text_input("Enter the starting country:")
    if st.button("Start Game"):
        if start_country in borders:
            st.session_state.current_country = start_country
            st.session_state.countries_visited.append(start_country)
            st.session_state.start_time = datetime.now()
        else:
            st.error("Invalid country. Please enter a valid country.")

# Function to process the next country
def next_country():
    next_country = st.text_input("Enter the next country:")
    if st.button("Submit"):
        if next_country in borders.get(st.session_state.current_country, []):
            if next_country not in st.session_state.countries_visited:
                st.session_state.current_country = next_country
                st.session_state.countries_visited.append(next_country)
            else:
                st.session_state.mistakes += 1
                st.error("Country already visited. Try a different country.")
        else:
            st.session_state.mistakes += 1
            st.error("Invalid move. The country does not border the previous one.")

        if all(country in st.session_state.countries_visited for country in borders[st.session_state.current_country]):
            st.session_state.end_time = datetime.now()
            st.info("Backtracking to the previous country.")
            for country in reversed(st.session_state.countries_visited):
                if any(neighbor not in st.session_state.countries_visited for neighbor in borders[country]):
                    st.session_state.current_country = country
                    break

# Display the game
def display_game():
    st.write(f"Current Country: {st.session_state.current_country}")
    st.write(f"Countries Visited: {', '.join(st.session_state.countries_visited)}")
    st.write(f"Mistakes: {st.session_state.mistakes}")
    if st.session_state.end_time:
        elapsed_time = st.session_state.end_time - st.session_state.start_time
        st.success(f"Congratulations! You finished the game in {elapsed_time}.")
    else:
        next_country()

# Main function
def main():
    st.title("World Traveler Game")
    if st.session_state.current_country is None:
        start_game()
    else:
        display_game()

if __name__ == "__main__":
    main()

