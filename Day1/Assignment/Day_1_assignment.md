
# Day_1 Assignment

## Objective
To automate the process of saving the output of the `date` command every 5 minutes into a file named `backup.txt`.

## Task Description
Create a shell script or use a scheduler like `cron` to execute the `date` command every 5 minutes and append its output to a file called `backup.txt`.

## Steps

### 1. Using `cron` (Recommended)
1. Open the crontab file using the following command:
   ```bash
   crontab -e
   ```
2. Add the following line to schedule the task every 5 minutes:
   ```bash
   */5 * * * * date >> /path/to/your/backup.txt
   ```
   Replace `/path/to/your/backup.txt` with the actual path where you want to store the file.

### 2. Verifying the Output
- Check the contents of `backup.txt` after some time to ensure entries are being added every 5 minutes.

## Note
Ensure that the path used in the cron job has the right permissions to write to `backup.txt`.

## Conclusion
This setup helps in creating time-based logs using the `date` command in an automated fashion.
