import { gql } from '@apollo/client'

export const MUTATION_AUDIO_PREDICT = gql`
  mutation ($audioFile: Upload!) {
    audioPredict(audioFile: $audioFile) {
      audioFile {
        id
        audioFile
        hashText
        result
      }
    }
  }
`
