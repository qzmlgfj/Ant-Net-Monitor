import { createStore } from 'vuex';

const store = createStore({
    state() {
        return {
            darkMode: false
        }
    },
    mutations: {
        changeTheme(state) {
            state.darkMode = state.darkMode == false ? true : false
        }
    }
})

export default store;
