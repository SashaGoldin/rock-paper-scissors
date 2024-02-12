import random
import streamlit as st


if 'rounds' not in st.session_state:
    st.session_state['rounds'] = []

st.title("The RPS Game")
st.image("therpsgame/therps.jpg", width=150)
st.subheader("Choose an option below and the computer will randomly pick one as well")
st.text("For additional details hover here ->", help="""
After each round you will see the result in the bottom right corner.

After 5 rounds the game's result will be announced.""")
st.markdown(" ")
phld = st.empty()

with phld.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        rock = st.button("Rock")
    with col2:
        paper = st.button("Paper")
    with col3:
        scissors = st.button("Scissors")


def compChoise():
    random_number = random.randint(1, 3)
    if random_number == 1:
        return "Rock"
    elif random_number == 2:
        return "Paper"
    else:
        return "Scissors"


def display_images(img1, img2):
    col4, col5, col6 = st.columns(3)
    with col4:
        st.image(f"therpsgame/{img1.lower()}.jpg", use_column_width=True, )
    with col5:
        st.text("<----- YOUR CHOICE  \n\n         VS  \n\n COMPUTER CHOICE -----> ")
    with col6:
        st.image(f"therpsgame/{img2.lower()}.jpg", use_column_width=True)


def game():
    if len(st.session_state.rounds) < 5:
        phld2 = st.empty()
        if rock:
            compTurn = compChoise()
            phld2.info("Computer choice is " + compTurn)
            display_images("rock", compTurn)

            if compTurn == "Rock":
                st.session_state.rounds.append("tie")
                st.toast("Tie")
            elif compTurn == "Paper":
                st.session_state.rounds.append("lost")
                st.toast("You lost")
            else:
                st.session_state.rounds.append("won")
                st.toast(":green[You Won!]")
        if paper:
            compTurn = compChoise()
            phld2.info("Computer choice is " + compTurn)
            display_images("paper", compTurn)
            if compTurn == "Rock":
                st.session_state.rounds.append("won")
                st.toast(":green[You Won!]")
            elif compTurn == "Paper":
                st.session_state.rounds.append("tie")
                st.toast("Tie")
            else:
                st.session_state.rounds.append("lost")
                st.toast("You lost")
        if scissors:
            compTurn = compChoise()
            phld2.info("Computer choice is " + compTurn)
            display_images("scissors", compTurn)
            if compTurn == "Rock":
                st.session_state.rounds.append("lost")
                st.toast("You lost")
            elif compTurn == "Paper":
                st.session_state.rounds.append("won")
                st.toast(":green[You Won!]")
            else:
                st.session_state.rounds.append("tie")
                st.toast("Tie")
        if len(st.session_state.rounds) == 5:
            phld.empty()
            phld2.empty()
            st.subheader("RESULT")
            for i, result in enumerate(st.session_state.rounds):
                st.write(i+1, result.upper())

            placeholder = st.empty()
            won_nr = st.session_state.rounds.count("won")
            lost_nr = st.session_state.rounds.count("lost")

            if won_nr > lost_nr:
                placeholder.success("Congrats you are the winner!!!")
                st.balloons()
            elif lost_nr > won_nr:
                placeholder.warning("Computer got lucky today")
            else:
                placeholder.info("No winners")
            st.session_state.rounds = []

            plc = st.empty()
            if plc.button("RESTART"):
                placeholder.empty()
                plc.empty()


game()




