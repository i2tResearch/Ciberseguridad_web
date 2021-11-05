import React from "react";

import { makeStyles } from "@material-ui/core/styles";
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
    root: {
      backgroundColor: "#121212",
      textAlign: "center",
      fontFamily: "Roboto",
      fontStyle: "light",
      color: "white",
    },
    button: {
        width: "280px",
        height: "50px",
        margin: "6%",
        backgroundColor: "white",
        color: "black",
        borderRadius: "20px",
        '&:hover': {
            backgroundColor: "lightgray",
        },
	},
}));

function Contact() {
    const classes = useStyles();

    return (
        <div className={classes.root}>
            <Typography variant="h1" style={{padding: "5%"}}>DeepDetector demo</Typography>
            <Button className={classes.button}><Typography variant="h5">Upload an audio</Typography></Button>
            <Typography variant="h2" style={{padding: "5%"}}>Result here</Typography>
        </div>
    )
}

export default Contact;
