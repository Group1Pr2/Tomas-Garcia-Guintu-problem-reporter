const { Provider } = require('ltijs');

Provider.setup(
  'your-secret-key-here',
  {
    url: 'mongodb+srv://delacruzcarloanthony7_db_user:q3TSWJzggNSwJHjL@cluster1.7hxec1t.mongodb.net/ltidb?retryWrites=true&w=majority',
  },
  {
    appRoute: '/app',
    loginRoute: '/lti/login',
    launchRoute: '/lti/launch',
    keysRoute: '/lti/jwks',
  }
);

Provider.onConnect(async (connection, res, next) => {
  const userName = connection.idToken.user.name || 'User';
  return res.redirect(`http://localhost:3000/dashboard?ltik=${connection.token}&name=${encodeURIComponent(userName)}`);
});

async function setup() {
  await Provider.deploy({ port: 4000 });
  console.log('LTI Server running on port 4000');
}

setup();