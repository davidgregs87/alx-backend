const app = function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array')
    }

    jobs.forEach((job) => {
        const jobProcess = queue.create('push_notification_code_3', job);

        jobProcess.on('enqueue', () => {
            console.log(`Notification job created: ${jobProcess.id}`)
        });

        jobProcess.on('complete', () => {
            console.log(`Notification job ${jobProcess.id} completed`)
        });

        jobProcess.on('failed', (err) => {
            console.error(`Notification job JOB_ID failed: ${err}`)
        });

        jobProcess.on('progress', (progress) => {
            console.log(`Notification job ${jobProcess.id} ${progress}% complete`)
        });

        jobProcess.save();
    })
}

module.exports = app;