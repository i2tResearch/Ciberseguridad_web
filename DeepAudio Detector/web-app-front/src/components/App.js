import React from 'react'
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import { ApolloClient, InMemoryCache, ApolloProvider } from '@apollo/client'
import { createUploadLink } from 'apollo-upload-client'
import { setContext } from '@apollo/client/link/context'

import Navbar from './Navbar'
import HomePage from '../pages/Home'
import Demo from '../pages/Demo'
import Paper from '../pages/Paper'
import Contact from '../pages/Contact'
import NotFound from '../pages/NotFound'
import Footer from '../components/Footer'

function App() {
  // Initialize Apollo Client
  const authLink = setContext((_, { headers }) => {
    return {
      headers: {
        ...headers
      }
    }
  })

  const httpLink = createUploadLink({
    uri: 'http://localhost:8000/graphql'
  })

  const client = new ApolloClient({
    link: authLink.concat(httpLink),
    cache: new InMemoryCache(),
    defaultOptions: { watchQuery: { fetchPolicy: 'cache-and-network' } }
  })
  return (
    <ApolloProvider client={client}>
      <BrowserRouter>
        <Navbar />
        <Switch>
          <Route exact path='/' component={HomePage} />
          <Route exact path='/demo' component={Demo} />
          <Route exact path='/paper' component={Paper} />
          <Route exact path='/contact' component={Contact} />
          <Route component={NotFound} />
        </Switch>
        <Footer />
      </BrowserRouter>
    </ApolloProvider>
  )
}

export default App
