import React from "react";

import { makeStyles } from "@material-ui/core/styles";
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';

import logo from "../images/logo.png";

const useStyles = makeStyles((theme) => ({
	root: {
		backgroundColor: "#353535",
		height: "315px",
		color: "white",
		fontFamily: "Roboto",
		textAlign: "center",
	},
	deep: {
		paddingTop: "6%",
	},
	grid: {
		padding: 0,
	},
	summary: {

	},
	contact: {
		paddingTop: "12%",
	},
    logo: {
        padding: "80px",
    },
}));

function Navbar() {
	const classes = useStyles();

	return (
		<div className={classes.root}>
            <Grid style={{padding: 0, width: "100%"}} container spacing={5} justify="center">
				<Grid item>
                    <img className={classes.logo} src={logo} alt="logo"/>
				</Grid>
				<Grid item>
					<Typography className={classes.deep} variant="h1">DeepDetector</Typography>
					<Typography className={classes.summary} variant="h5">Detect deepfake audios in seconds</Typography>
				</Grid>
			</Grid>
			<Typography variant="h5">Terms and Conditions | Privacy Policy | Frequently Asked Questions | Contact Us</Typography>
			<Typography variant="h5">© Copyright 2021 Deepdetector.com All rights reserved</Typography>
		</div>
	);
}

export default Navbar;
