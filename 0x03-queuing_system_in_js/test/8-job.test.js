import { createPushNotificationsJobs } from './8-job.js';
import { createQueue } from 'kue';

describe('createPushNotificationsJobs', () => {
    const queue = createQueue()
    
    beforeAll(() => {
        queue.testMode.enter();
    })

    afterAll(() => {
        queue.testMode.clear();
        queue.testMode.exit();
    })

    it('should enqueue jobs into the queue', async () => {
        testJobs = [
            {
                phoneNo : '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
               phoneNo : '4153394683',
               message: 'This is the code 1234 to verify your account' 
            }
        ];

        createPushNotificationsJobs(testJobs, queue)

        expect(queue.testMode.jobs.length).toBe(testJobs.length)
        expect(queue.testMode.jobs.length).to.equal(2)
        expect(queue.testMode.jobs[0].data).to.eql({phoneNo : '4153518780', message: 'This is the code 1234 to verify your account'})
    })
})