#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:47:53 2026

@author: umarfarooq
"""

# 1. Import af bibliotek
import streamlit as st

# 2. Titel på appen
st.title("Gæt sangen ud fra lyrikken")

# 3. Definér quiz-spørgsmål
questions = [
    {
        "lyric": "I came in like a...",
        "correct": "Wrecking Ball",
        "options": ["Wrecking Ball", "Flowers", "Bad Romance", "Shake It Off"]
    },
    {
        "lyric": "Is it too late now to...",
        "correct": "Sorry",
        "options": ["Sorry", "Stay", "Peaches", "Love Yourself"]
    },
    {
        "lyric": "Cause the players gonna play...",
        "correct": "Shake It Off",
        "options": ["Blank Space", "Shake It Off", "Style", "Anti-Hero"]
    }
]

# 4. Initialisering af session state (gemmer fremgang og score)
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False

# 5. Vis aktuelt spørgsmål (hvis quiz ikke er færdig)
if st.session_state.current_question < len(questions):
    q = questions[st.session_state.current_question]

    st.write(f"Spørgsmål {st.session_state.current_question + 1} af {len(questions)}")
    st.subheader("Hvilken sang stammer denne lyrik fra?")
    st.info(f"“{q['lyric']}”")

    # 6. Brugerens svar (multiple choice)
    answer = st.radio(
        "Vælg et svar:",
        q["options"],
        index=None,
        key=st.session_state.current_question
    )

    # 7. Tjek om svaret er korrekt
    if st.button("Tjek svar"):
        if answer is None:
            st.warning("Vælg et svar først.")
        else:
            st.session_state.answered = True

            if answer == q["correct"]:
                st.session_state.score += 1
                st.success("Korrekt.")
            else:
                st.error(f"Forkert. Det rigtige svar var: {q['correct']}")

    # 8. Gå videre til næste spørgsmål
    if st.session_state.answered:
        if st.button("Næste spørgsmål"):
            st.session_state.current_question += 1
            st.session_state.answered = False
            st.rerun()

# 9. Vis slutresultat når quizzen er færdig
else:
    st.success("Quizzen er færdig.")
    st.write(f"Du fik {st.session_state.score} ud af {len(questions)} rigtige.")

    # 10. Start quizzen forfra
    if st.button("Start forfra"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()



