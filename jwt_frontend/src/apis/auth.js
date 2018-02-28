import axios from 'axios'

const HOST = 'http://localhost:12345/api/v1'
const LoginURL = `${HOST}/auth`

export const doLogin = (loginData) => (
    axios.post(LoginURL, loginData)
)

const LogoutURL = `${HOST}/user/logout`
export const doLogout = (token) => (
    axios.post(LogoutURL, {}, { headers: { Authorization: `JWT ${token}` } })
)

const PasswordResetURL = `${HOST}/user/passwordreset`
export const doResetPassword = (token, oldpassword, newpassword) => (
    axios.post(PasswordResetURL, { password: oldpassword, newpassword: newpassword },
        { headers: { Authorization: `JWT ${token}` } })
)