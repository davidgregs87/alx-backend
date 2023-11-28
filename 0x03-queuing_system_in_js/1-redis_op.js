import { createClient } from 'redis';
import { print } from 'redis';

const client = createClient()

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
    client.SET(schoolName, value, (err, res) => {
      print(err, res)
    })
}

function displaySchoolValue(schoolName) {
    client.GET(schoolName, (err, res) => {
      if (err) {
        console.error(err)
        } else {
        console.log(res)
        }
    })
}


client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`)
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
