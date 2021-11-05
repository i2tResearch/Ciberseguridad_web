import React from 'react'

import { makeStyles } from '@material-ui/core/styles'
import Typography from '@material-ui/core/Typography'
import Button from '@material-ui/core/Button'
import Grid from '@material-ui/core/Grid'

import background from '../images/background.png'
import secure from '../images/secure.png'
import key from '../images/key.png'
import cloud from '../images/cloud.png'
import { useState } from 'react'
import { useMutation } from '@apollo/client'
import { MUTATION_AUDIO_PREDICT } from '../graphql/mutationAudioPredict'

const useStyles = makeStyles(theme => ({
  root: {
    backgroundColor: '#121212',
    textAlign: 'center',
    fontFamily: 'Roboto',
    fontStyle: 'light',
    color: 'white'
  },
  main: {
    margin: 0,
    width: '100%',
    height: '752px'
  },
  features: {
    margin: '50px'
  },
  card: {
    backgroundColor: '#3b3b3b',
    width: '300px',
    minHeight: '191px'
  },
  deep: {
    paddingTop: '18%'
  },
  summary: {},
  howUse: {
    padding: '80px'
  },
  inputFileHide: {
    overflow: 'hidden',
    width: 0,
    height: 0
  },
  buttonFile: {
    cursor: 'pointer',
    backgroundColor: '#FFF',
    color: '#000',
    margin: '100px',
    borderRadius: '20px',
    position: 'relative',
    display: 'flex',
    width: '280px',
    height: '50px',
    justifyContent: 'center',
    alignItems: 'center',
    '&:hover': {
      backgroundColor: 'lightgray'
    }
  },
  containerFileButton: {
    display: 'flex',
    justifyContent: 'center'
  },
  containerLoading: {
    margin: '100px'
  }
}))

function Home() {
  const classes = useStyles()
  const [selectedFile, setSelectedFile] = useState()
  const [isFilePicked, setIsFilePicked] = useState(false)

  const [SendAudioPredict, { loading, error, data }] = useMutation(
    MUTATION_AUDIO_PREDICT
  )

  const changeHandler = e => {
    setSelectedFile(e.target.files[0])
    setIsFilePicked(true)
  }

  const sendData = () => {
    SendAudioPredict({
      variables: {
        audioFile: selectedFile
      }
    })
  }

  return (
    <div className={classes.root}>
      <div
        className={classes.main}
        style={{ backgroundImage: `url(${background})` }}
      >
        <Typography className={classes.deep} variant='h1'>
          DeepDetector
        </Typography>
        <Typography className={classes.summary} variant='h5'>
          Detect deepfake audios in seconds
        </Typography>
      </div>
      <div>
        <Typography className={classes.features} variant='h2'>
          Features
        </Typography>
        <Grid
          style={{ paddingBottom: '5%', width: '100%' }}
          container
          spacing={10}
          justify='center'
        >
          <Grid item>
            <div className={classes.card}>
              <img src={secure} alt='secure logo' />
              <Typography variant='h4'>Secure</Typography>
            </div>
          </Grid>
          <Grid item>
            <div className={classes.card}>
              <img src={key} alt='key logo' />
              <Typography variant='h4'>Secure</Typography>
            </div>
          </Grid>
          <Grid item>
            <div className={classes.card}>
              <img src={cloud} alt='cloud logo' />
              <Typography variant='h4'>Secure</Typography>
            </div>
          </Grid>
        </Grid>
      </div>
      <div className={classes.containerFileButton}>
        {error ? (
          <p className={classes.containerLoading}>ERROR MUTACION...</p>
        ) : loading ? (
          <p className={classes.containerLoading}>Loading...</p>
        ) : data ? (
          <div>
            <p>DETAILS</p>
            <p>AudioFile: {data.audioPredict.audioFile.audioFile}</p>
            <p>HashText: {data.audioPredict.audioFile.hashText}</p>
                <p>Result: The audio is {(Math.round(data.audioPredict.audioFile.result * 100) / 100) *100}% Real</p>
          </div>
        ) : isFilePicked ? (
          <Button className={classes.buttonFile} onClick={sendData}>
            <Typography variant='h5'>Send audio</Typography>
          </Button>
        ) : (
          <>
            <input
              type='file'
              className={classes.inputFileHide}
              onChange={changeHandler}
              id='fileHandler'
              accept='audio/*'
            />
            <label htmlFor='fileHandler' className={classes.buttonFile}>
              <Typography variant='h5'>Upload an audio</Typography>
            </label>
          </>
        )}
      </div>
      <hr style={{ width: '75%' }} />
      <div className={classes.howUse}>
        <Typography variant='h2' style={{}}>
          How to use
        </Typography>
        <Typography variant='h3' style={{ paddingTop: '100px' }}>
          1. Upload an video
        </Typography>
        <Typography variant='h3' style={{ paddingTop: '100px' }}>
          2. Wait until completion
        </Typography>
        <Typography variant='h3' style={{ paddingTop: '100px' }}>
          3. Done
        </Typography>
        <Typography variant='h4' style={{}}>
          Now you can check the result
        </Typography>
      </div>
    </div>
  )
}

export default Home
