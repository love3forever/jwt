import React, { Component } from 'react'
import {doGetUserInfo} from '../apis/auth'

export default class PublicPage extends Component {
    constructor(props){
        super(props)
        this.state={
            response:''
        }
    }

    componentDidMount(){
        let token = localStorage.getItem('jwtToken')
        doGetUserInfo(token)
        .then(response=>{
            console.log(response)
            this.setState({
                response:response.data.username
            })
        })
        .catch(error=>{
            console.log(error.response.data)
            this.setState({
                response:error.response.data
            })
        })
    }

  render() {
    return (
      <div>
        <h1>{this.state.response}</h1>
      </div>
    )
  }
}
