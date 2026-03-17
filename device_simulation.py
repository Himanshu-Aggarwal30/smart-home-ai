import random
import streamlit as st


def simulate_devices(room, devices):

    safe_room = room.replace(" ", "_")

    for device in devices:

        key = f"{safe_room}_{device}_power"
        sim_key = f"{key}_sim"

        if random.random() < 0.3:

            if device.lower() == "light":
                st.session_state[sim_key] = random.uniform(0.05, 0.15)

            elif device.lower() == "fan":
                st.session_state[sim_key] = random.uniform(0.08, 0.25)

            elif device.lower() == "ac":
                st.session_state[sim_key] = random.uniform(0.8, 1.5)

            else:
                st.session_state[sim_key] = random.uniform(0.05, 0.3)

        else:
            st.session_state[sim_key] = 0