import React, { Component } from 'react'
import { doResetPassword } from '../apis/auth'
import { connect } from 'react-redux'
import { push } from 'react-router-redux'

class PasswordResetPage extends Component {

  constructor(props) {
    super(props)
    this.state = {
      oldPassword: '',
      newPassword: '',
      errorMsg: '',
      successMsg: '',
      isPasswordReseted: false
    }
  }

  componentDidMount() {
    if (!localStorage.getItem('jwtToken')) {
      let {dispatch} = this.props
      dispatch(push('/'))
    }
  }

  handleOldPasswordChange = (e) => {
    this.setState({
      oldPassword: e.target.value
    })
  }

  handleNewPasswordChange = (e) => {
    this.setState({
      newPassword: e.target.value
    })
  }

  handlePasswordReset = (e) => {
    e.preventDefault()
    let token = localStorage.getItem('jwtToken')
    if (this.state.oldPassword && this.state.newPassword) {
      doResetPassword(token, this.state.oldPassword, this.state.newPassword)
        .then(response => {
          console.log(response.data)
          this.setState({
            successMsg: response.data.msg,
            isPasswordReseted: true
          })
          localStorage.removeItem('jwtToken')
        })
        .catch(error => {
          console.log(error.response.data)
          this.setState({
            errorMsg: error.response.data.message
          })
        })
    }
  }

  render() {
    return (
      <div>
        <h1>
          password reset
        </h1>
        {!this.state.isPasswordReseted &&
          <form>
            <label>
              Old Password:
        <input type="password" value={this.state.oldPassword} onChange={this.handleOldPasswordChange} />
            </label>
            <label>
              New Password:
        <input type="password" value={this.state.newpassword} onChange={this.handleNewPasswordChange} />
            </label>
            {/* <input type="submit" value="Submit" /> */}
            <button onClick={this.handlePasswordReset}>Submit</button>
          </form>
        }
        <h2>{this.state.errorMsg || this.state.successMsg}</h2>
      </div >
    )
  }
}

export default connect()(PasswordResetPage)