import React, { Component } from 'react'
import { connect } from 'react-redux';
import { push } from 'react-router-redux'
import { withRouter } from 'react-router-dom'

import { doLogin } from '../apis/auth'

class LoginPage extends Component {
    constructor(props) {
        super(props)
        this.state = {
            'username': '',
            'password': ''
        }
    }


    handlePasswordChange = (e) => {
        this.setState({
            'password': e.target.value
        })
    }

    handleUsernameChange = (e) => {
        this.setState({
            'username': e.target.value
        })
    }

    handleLogin = (e) => {
        // 此处必须要有preventDefault操作
        e.preventDefault()
        let { dispatch } = this.props
        let loginData = {
            username: this.state.username,
            password: this.state.password
        }
        console.log(loginData)
        if (this.state.username && this.state.password) {
            doLogin(loginData).then((response) => {
                console.log(response)
                localStorage.setItem('jwtToken', response.data.access_token)
                dispatch(push('/'))
            })
            .catch((error) => {
                console.log(error.response.data)
            })
        }
    }

    render() {
        return (
            <div>
                <h1>
                    请先完成登陆！
        </h1>
                <form>
                    <label>
                        Username:
                <input type="text" value={this.state.username} onChange={this.handleUsernameChange} />
                    </label>
                    <label>
                        Password:
                <input type="password" value={this.state.password} onChange={this.handlePasswordChange} />
                    </label>
                    {/* <input type="submit" value="Submit" /> */}
                    <button onClick={this.handleLogin}>Submit</button>
                </form>
            </div>
        )
    }
}


export default withRouter(connect()(LoginPage))