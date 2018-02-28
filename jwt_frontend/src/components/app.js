import React, { Component } from 'react'
import { push } from 'react-router-redux'
import { withRouter, Link } from 'react-router-dom'
import { connect } from 'react-redux';

class App extends Component {
    componentDidMount() {
        console.log('home page mounted')
        let token = localStorage.getItem('jwtToken') || this.props.jwtToken
        let { dispatch } = this.props
        if (!token) {
            dispatch(push('/login'))
        }
    }

    render() {
        return (
            <div>
                <h1>你已完成登陆</h1>
                <ul>
                    <li>
                        <Link to="/logout">登出</Link>
                    </li>
                    <li>
                        <Link to="/reset">重置密码</Link>
                    </li>
                </ul>
            </div>
        )
    }
}


const mapStateToProps = (state) => {
    const { jwtToken } = state

    return { jwtToken }
}

export default withRouter(connect(mapStateToProps)(App))

