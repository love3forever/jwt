import React, { Component } from 'react'
import { doLogout } from '../apis/auth'

export default class LogoutPage extends Component {
  componentDidMount() {
    let token = localStorage.getItem('jwtToken')
    if (token) {
      localStorage.removeItem('jwtToken')
      doLogout(token)
        .then(response => {
          console.log(response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }

  }

  render() {
    return (
      <div>
        <h1>
          logout
        </h1>
      </div>
    )
  }
}
