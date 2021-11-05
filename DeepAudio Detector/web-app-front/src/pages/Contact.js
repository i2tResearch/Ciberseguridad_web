import React from "react";

import { makeStyles } from "@material-ui/core/styles";
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
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
		margin: "100px",
        backgroundColor: "white",
        color: "black",
        borderRadius: "20px",
        '&:hover': {
            backgroundColor: "lightgray",
        },
	},
    main: {
        width: "100%",
        height: "750px",
        paddingTop: "250px"
    },
    card: {
        backgroundColor: "#3b3b3b",
        width: "300px"
    },
}));

function Contact() {
	const classes = useStyles();

    return (
        <div className={classes.root}>
            <div className={classes.main}>
                <Typography variant="h2">We help you identify altered audios</Typography>
                <Button className={classes.button}><Typography variant="h5">Upload an audio</Typography></Button>
            </div>
            <Typography style={{padding: "5%"}} variant="h2">Contact us</Typography>
            <Grid style={{paddingBottom: "5%", width: "100%"}} container spacing={10} justify="center">
                <Grid item>
                    <div className={classes.card}>
                        <Typography variant="h4">Cristhian Castillo<br/>email<br/>github</Typography>
                    </div>
                </Grid>
                <Grid item>
                    <div className={classes.card}>
                        <Typography variant="h4">Kevin Zarama<br/>email<br/>github</Typography>
                    </div>
                </Grid>
                <Grid item>
                    <div className={classes.card}>
                        <Typography variant="h4">Cristian Urcuqui<br/>email<br/>github</Typography>
                    </div>
                </Grid>
            </Grid>
        </div>
    )
}

export default Contact;
