import React from 'react';
import { View, Text, Button } from 'react-native';

class HomeScreen extends React.Component {
    static navigationOptions = {
        title: 'Home',
    };
    render() {
        const { navigate } = this.props.navigation;
        return (
            <Button
                title="Go to Detail"
                onPress={() =>
                    navigate('Detail', { name: 'Jane' })
                }
            />
        );
    }
}

export default HomeScreen;
