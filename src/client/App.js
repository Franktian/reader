import { StackNavigator } from 'react-navigation';

import HomeScreen from './javascripts/HomeScreen';
import DetailScreen from './javascripts/DetailScreen';

const App = StackNavigator({
  Home: { screen: HomeScreen },
  Detail: { screen: DetailScreen },
});

export default App;
