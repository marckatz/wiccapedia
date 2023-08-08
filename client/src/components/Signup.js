import React, { useState } from 'react';
import { useFormik } from "formik";
import * as yup from "yup";
import {useHistory} from 'react-router-dom';

function Signup({handleUser}) {

  // const [password, setPassword] = useState('');
  // const [errors, setErrors] = useState({ username: '', password: '' });
  const history = useHistory();

  // const handleSignup = () => {
  //   let isValid = true;

  //   // Reset errors
  //   setErrors({ username: '', password: '' });

  //   // Validate username and password length
  //   if (username.length < 6) {
  //     setErrors((prevErrors) => ({ ...prevErrors, username: 'username too short!' }));
  //     isValid = false;
  //   }

  //   if (password.length < 6) {
  //     setErrors((prevErrors) => ({ ...prevErrors, password: 'password too short!' }));
  //     isValid = false;
  //   }

    // Check if username exists
    // if () {
    // setErrors((prevErrors) => ({ ...prevErrors, username: 'username already exists!' }));
  //   // isValid = false
  //   // }

  //   if (isValid) {
  //     // bulabula
  //   }
  // };

  const formSchema = yup.object().shape({
    // email: yup.string().email("Invalid email").required("Must enter email"),
    username: yup.string().required("Must enter a name").min(5).max(25),
    password: yup.string().required("Must enter a password").min(6).max(15),
  });

  const formik = useFormik({
    initialValues: {
      username: "",
      password: "",
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      fetch('/users', {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values, null, 2),
      }).then(
        (res) => {
          if (res.ok){
            res.json()
            .then(data => {
              handleUser(data.username)
              history.push('/')
            })
          }
          else{
            res.json()
            .then(data => console.log(data))         
          }
        }
      )
    },
  });

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-4">
          <h2 className="text-center">Signup</h2>
          <form onSubmit={formik.handleSubmit}>
            <div className="row-mb-1">
              <label htmlFor='username' className='form-label'>Username:</label>
              <input
                type="text"
                // className={`form-control ${errors.username && 'is-invalid'}`}
                className={`form-control`}
                value={formik.values.username}
                onChange={formik.handleChange}
                name = 'username'
                id = 'username'
                required
              />
              {/* {errors.username && <div className="invalid-feedback">{errors.username}</div>} */}
              <p style={{color : "red"}}> {formik.errors.username}</p>
            </div>
            <div className="row-mb-1">
              <label className='form-label'>Password:</label>
              <input
                type="password"
                className={`form-control`}
                value={formik.values.password}
                name = 'password'
                id = 'password'
                onChange={formik.handleChange}
                required
              />
              <p style={{color : "red"}}> {formik.errors.password}</p>
            </div>
            <div className="text-center">
              <button className="btn btn-warning" type="submit">
                Signup
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Signup;
