import React, { useState } from 'react';
import { useFormik } from "formik";
import * as yup from "yup";
import { useHistory } from 'react-router-dom';

function Signup({ handleUser }) {
  const history = useHistory();
  const [serverError, setServerError] = useState('');

  const formSchema = yup.object().shape({
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
      }).then((res) => {
        if (res.ok) {
          res.json().then(data => {
            handleUser(data.username);
            history.push('/');
          });
        } else {
          res.json().then(data => {
            setServerError(data.error || "An error occurred during registration.");
          });
        }
      });
    },
  });

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-4">
          <h2 className="text-center">Signup</h2>
          {serverError && <div className="alert alert-danger">{serverError}</div>} {/* <- Display server error */}
          <form onSubmit={formik.handleSubmit}>
            <div className="mb-1">
              <label htmlFor='username' className='form-label'>Username:</label>
              <input
                type="text"
                className="form-control"
                value={formik.values.username}
                onChange={formik.handleChange}
                name='username'
                id='username'
                required
              />
              <p style={{ color: "red" }}>{formik.errors.username}</p>
            </div>
            <div className="mb-1">
              <label className='form-label'>Password:</label>
              <input
                type="password"
                className="form-control"
                value={formik.values.password}
                name='password'
                id='password'
                onChange={formik.handleChange}
                required
              />
              <p style={{ color: "red" }}>{formik.errors.password}</p>
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
