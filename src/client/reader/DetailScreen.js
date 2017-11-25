import React from 'react';
import { View, Text } from 'react-native';

class DetailScreen extends React.Component {
    static navigationOptions = {
        title: 'Detail',
    };
    render() {
        return (
            <View>
                <Text>Details</Text>
            </View>
        );
    }
}

export default DetailScreen;
