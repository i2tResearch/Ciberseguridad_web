import React from "react";
import { Link } from "react-router-dom";

import { makeStyles } from "@material-ui/core/styles";
import Button from '@material-ui/core/Button';

import logo from "../images/logo.png";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    boxSizing: "border-box",
    margin: 0,
    padding: 0,
    height: 55,
    backgroundColor: "#24252a",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    textAlign: "center",
    textDecoration: "none",
  },
  Links: {
    color: "#edf0f1",
    fontSize: 14,
    textDecoration: "none",
    "&:hover": {
      color: "lightgray",
    },
  },
  li: {
    color: "#edf0f1",
    textDecoration: "none",
    display: "inline-block",
    padding: "0px 20px",
    transition: "all 0.3s ease 0s",
  },
  ul: {
    position: "absolute",
    right: "1%",
    top: "-7px",
    listStyle: "none",
  },
  logo: {
    position: "absolute",
    left: "1%",
    },
  button: {
    backgroundColor: "white",
    color: "black",
    borderRadius: "20px",
    '&:hover': {
      backgroundColor: "lightgray",
    },
  },
}));

function Navbar() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <img className={classes.logo} src={logo} alt="logo"/>
      <nav>
        <ul className={classes.ul}>
          <li className={classes.li}><Link to="/" className={classes.Links}>Home</Link></li>
          <li className={classes.li}><Link to="/demo" className={classes.Links}>Demo</Link></li>
          <li className={classes.li}><Link to="/paper" className={classes.Links}>Paper</Link></li>
          <li className={classes.li}><Link to="/contact" className={classes.Links}><Button variant="contained" color="primary" className={classes.button}>Contact us</Button></Link></li>
        </ul>
      </nav>
    </div>
  );
}

export default Navbar;
