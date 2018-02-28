import React from 'react'
import ReactDOM from 'react-dom'

import { createStore, combineReducers, applyMiddleware } from 'redux'
import { Provider } from 'react-redux'

import createHistory from 'history/createBrowserHistory'
import { Route } from 'react-router'

import { ConnectedRouter, routerReducer, routerMiddleware } from 'react-router-redux'

import reducers from './reducers' // Or wherever you keep your reducers

import App from './components/app'
import Login from './components/login'
import Logout from './components/logout'
import PasswordReset from './components/passwordreset'
import Register from './components/register'
<<<<<<< HEAD
import PublicPage from './components/public'
=======
>>>>>>> 4456a8699933a1bb23d4843dcf0f140d5fd0191c

// Create a history of your choosing (we're using a browser history in this case)
const history = createHistory()

// Build the middleware for intercepting and dispatching navigation actions
const middleware = routerMiddleware(history)

// Add the reducer to your store on the `router` key
// Also apply our middleware for navigating
const store = createStore(
    combineReducers({
        ...reducers,
        router: routerReducer
    }),
    applyMiddleware(middleware)
)

// Now you can dispatch navigation actions from anywhere!
// store.dispatch(push('/foo'))

ReactDOM.render(
    <Provider store={store}>
        { /* ConnectedRouter will use the store from Provider automatically */}
        <ConnectedRouter history={history}>
            <div>
                <Route exact path="/" component={App} />
                <Route path="/login" component={Login} />
                <Route path="/logout" component={Logout} />
                <Route path="/reset" component={PasswordReset} />
                <Route path="/register" component={Register}></Route>
                <Route path="/public" component={PublicPage}></Route>
            </div>
        </ConnectedRouter>
    </Provider>,
    document.getElementById('root')
)