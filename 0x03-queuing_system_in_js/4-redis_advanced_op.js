import { createClient } from "redis";
import { print } from "redis";

const client = createClient()

client.HSET('HolbertonSchools', 'Portland', 50, (err, res) => {
    print(err, res);
});
client.HSET('HolbertonSchools', 'Seattle', 80, (err, res) => {
    print(err, res);
});
client.HSET('HolbertonSchools', 'New York', 20, (err, res) => {
    print(err, res);
});
client.HSET('HolbertonSchools', 'Bogota', 20, (err, res) => {
    print(err, res);
});
client.HSET('HolbertonSchools', 'Cali', 40, (err, res) => {
    print(err, res);
});
client.HSET('HolbertonSchools', 'Paris', 2, (err, res) => {
    print(err, res);
});

client.HGETALL('HolbertonSchools', (err, res) => {
    if (err) {
        console.error(err);
    } else {
        console.log(res);
    }
});