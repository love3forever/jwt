import React, { Component } from 'react'
import { connect } from 'react-redux'
import { push } from 'react-router-redux'
import { withRouter } from 'react-router-dom'

import {doRegister} from '../apis/auth'


class RegisterPage extends Component {
    constructor(props){
        super(props)
        this.state = {
            username:'',
            password:''
        }
    }


    componentDidMount() {
        if(localStorage.getItem('jwtToken')){
            let {dispatch} = this.props
            dispatch(push('/logout'))
        }
    }

    handleRegister = (e) => {
        e.preventDefault()
        let {dispatch} = this.props
        if(this.state.username && this.state.password){
            doRegister(this.state.username,this.state.password)
            .then(response=>{
                console.log(response.data)
                dispatch(push('/'))
            })
            .catch(error=>{
                console.log(error.response.data.message)
            })
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

    render() {
        return (
            <div>
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
                    <button onClick={this.handleRegister}>Submit</button>
                </form>
            </div>
        )
    }
}


export default withRouter(connect()(RegisterPage))