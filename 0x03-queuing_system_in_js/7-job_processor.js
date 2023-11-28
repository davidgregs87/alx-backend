import { createQueue } from "kue";

const queue = createQueue()

const blackLists = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0);

    if (blackLists.includes(phoneNumber)) {
        done(new Error(`Phone number ${phoneNumber} is blacklisted`))
    }

    job.progress(50);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}

queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;

    sendNotification(phoneNumber, message, job, done)

    done();
})

queue.on('complete', (id) => {
    console.log(`Job ${id} completed`);
})

queue.on('failed', (id, err) => {
    console.log(`Job ${id} failed: ${err.message}`);
})