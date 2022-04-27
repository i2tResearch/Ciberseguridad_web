import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"; 

Vue.use(Vuex);

export default new Vuex.Store({
    plugins:[createPersistedState()],
    state: {
        backend:'http://localhost:5000',
        dir_routes:{
            dash:'Dash',
            login:'Login',
            about:'About'
        },
        isWaiting:true,
        authenticated:false,
        email:''
    },
    mutations: {
        updateDashState(state,dashState){
            state.isWaiting = dashState;
        },
        updateAuthentication(state,auth){
            state.authenticated = auth;
        },
        updateEmail(state,email){
            state.email = email;
        }
    },
    actions: {
        updateDashStates({ commit }, token){
            commit('updateDashState',token);
        }, 
        updateAuthenticationState({ commit }, token){
            commit('updateAuthentication', token);
        },
        updateEmailApp({ commit }, token){
            commit('updateEmail', token);
        }

    },
})