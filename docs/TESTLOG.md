# Test Log

Asked the app 5 questions and wrote down what happened. First 4 are stuff
thats actually in my docs, last one isnt, just to see what it does. This
is copy pasted straight from a real terminal run of `uv run python main.py`.

- embedding model: nomic-embed-text (Ollama)
- gen model: gemma4 (Ollama)
- vector store: ChromaDB (chroma_db/)
- chunking: fixed size, 800 chars, 160 overlap

run `uv run python main.py` to try it yourself. heads up — the retrieved
chunks will always be the same for the same question (thats deterministic,
its just math), but the generated answer text will read a bit different
every time you run it, since the model doesnt use a fixed seed. thats
normal, not a bug.

---

## Q1. How do I configure VPN access for remote workers?

_in my docs: yes - took about 24s_

```
----- Retrieved chunks -----
Chunk 1:
**Configuring VPN Access for Remote Workers**

**Overview**

This article provides step-by-step instructions for configuring VPN access for remote workers. This allows employees working from home or other remote locations to securely connect to the company network and access company resources.

**Prerequisites**

* The remote worker's device (laptop or desktop) must meet the company's minimum syst ...

Chunk 2:
you are unable to access company resources, verify that you are connected to the VPN and that your device's IP address has changed to a company-assigned IP address.
* If you continue to experience issues, contact the IT helpdesk for further assistance.

**Security Reminders**

* Always keep your VPN client software up-to-date.
* Never share your login credentials with anyone.
* Avoid using public  ...

Chunk 3:
nd download the VPN client software.
2. Run the installer and follow the prompts to install the software.
3. Once installed, launch the VPN client software.

**Step 2: Configure the VPN Connection**

1. In the VPN client software, click on "New Connection" and select "Company VPN" as the connection type.
2. Enter the company's VPN server address: `vpn.company.com`.
3. Enter your company login cred ...
---------------------------
```

**Answer:**
```
To configure VPN access for remote workers, follow these steps:

**Prerequisites:**
Before starting, ensure that:
*   Your device meets the company's minimum system requirements for VPN connectivity.
*   You have valid company login credentials.
*   You have a stable internet connection.

**Step 1: Install the VPN Client**
1.  Go to the company's software portal and download the VPN client software.
2.  Run the installer and follow the prompts to install the software.
3.  Once installed, launch the VPN client software.

**Step 2: Configure the VPN Connection**
1.  In the VPN client software, click on "New Connection" and select "Company VPN" as the connection type.
2.  Enter the company's VPN server address: `vpn.company.com`.
3.  Enter your company login credentials (username and password).
4.  Select the "Save" button to save the connection settings.

**Step 3: Establish the VPN Connection**
1.  Click on the "Connect" button to establish the VPN connection.
2.  Follow the prompts to complete two-factor authentication (2FA) if you are prompted.
3.  Once connected, you will see a confirmation message.

If you are unable to access company resources after following these steps, verify that you are connected to the VPN and that your device's IP address has changed to a company-assigned IP address. If issues continue, contact the IT helpdesk for further assistance.
```

---

## Q2. What should I do if I have forgotten my PIN?

_in my docs: yes - took about 29s_

```
----- Retrieved chunks -----
Chunk 1:
are unable to reset your PIN using the self-service tool, please contact the IT Helpdesk for assistance.
* It is recommended to keep your PIN confidential and not share it with anyone.
* You can reset your PIN a maximum of 3 times in a 24-hour period. If you exceed this limit, you will need to contact the IT Helpdesk to reset your PIN.

By following these steps, you should be able to reset your fo ...

Chunk 2:
**Resetting a Forgotten PIN**

If you have forgotten your PIN, you can reset it using the following steps:

**Step 1: Access the PIN Reset Tool**

1. Go to the company's intranet homepage and click on the "IT Support" link at the top right corner of the page.
2. Click on the "Self-Service" tab and then select "PIN Reset" from the drop-down menu.
3. You will be redirected to the PIN Reset Tool logi ...

Chunk 3:
our security question. Enter your answer in the required field.
2. Click the "Next" button to proceed.

**Step 4: Reset Your PIN**

1. Enter a new PIN in the required field. The PIN must be at least 8 characters long and contain a mix of uppercase and lowercase letters, numbers, and special characters.
2. Re-enter your new PIN in the confirmation field to ensure accuracy.
3. Click the "Reset PIN"  ...
---------------------------
```

**Answer:**
```
To reset a forgotten PIN, follow these steps:

**Step 1: Access the PIN Reset Tool**
1. Go to the company's intranet homepage and click on the "IT Support" link at the top right corner of the page.
2. Click on the "Self-Service" tab and then select "PIN Reset" from the drop-down menu.
3. You will be redirected to the PIN Reset Tool login page.

**Step 2: Authenticate with Your Credentials**
1. Enter your company username and password in the required fields.
2. Click the "Login" button to authenticate.

**Step 3: Verify Your Identity**
1. You will be prompted to answer your security question. Enter your answer in the required field.
2. Click the "Next" button to proceed.

**Step 4: Reset Your PIN**
1. Enter a new PIN in the required field. The PIN must be at least 8 characters long and contain a mix of uppercase and lowercase letters, numbers, and special characters.
2. Re-enter your new PIN in the confirmation field to ensure accuracy.
3. Click the "Reset PIN" button to complete the process.

**Step 5: Confirm PIN Reset**
1. You will receive a confirmation message indicating that your PIN has been successfully reset.
2. Click the "OK" button to close the message.

**Important Notes:**
* It is recommended to keep your PIN confidential and not share it with anyone.
* You can reset your PIN a maximum of 3 times in a 24-hour period. If you exceed this limit, you will need to contact the IT Helpdesk to reset your PIN.
* If you are unable to reset your PIN using the self-service tool, please contact the IT Helpdesk for assistance.
```

---

## Q3. How do I set up a conference call on Cisco Webex?

_in my docs: yes - took about 13s_

```
----- Retrieved chunks -----
Chunk 1:
To set up a conference call on Cisco Webex, follow these steps:

**Step 1: Log in to Cisco Webex**

Open a web browser and navigate to [company Webex URL]. Enter your company login credentials to access the Webex portal.

**Step 2: Schedule a Meeting**

Click on the "Meetings" tab and select "Schedule a Meeting" from the drop-down menu. Fill in the required information, including:

* Meeting topic ...

Chunk 2:
o allow participants to join via phone or VoIP.

**Step 4: Set Up Video Settings (Optional)**

If you want to enable video conferencing, click on the "Video" tab and select "Cisco Webex Video" as the default video type. You can also choose to allow participants to join via video.

**Step 5: Add Agenda and Notes (Optional)**

You can add an agenda and notes to the meeting invitation by clicking on  ...

Chunk 3:
cipants.

**Troubleshooting**

* If you encounter issues joining the meeting, try restarting your browser or checking your internet connection.
* If you experience audio or video issues during the meeting, try restarting your audio or video settings or contacting the IT helpdesk for assistance.

By following these steps, you can successfully set up and host a conference call on Cisco Webex. If you ...
---------------------------
```

**Answer:**
```
To set up a conference call on Cisco Webex, follow these steps:

**Step 1: Log in to Cisco Webex**
Open a web browser and navigate to [company Webex URL]. Enter your company login credentials to access the Webex portal.

**Step 2: Schedule a Meeting**
Click on the "Meetings" tab and select "Schedule a Meeting" from the drop-down menu. Fill in the required information, including:
* Meeting topic
* Start and end time
* Duration
* Invitees (add email addresses or names from the company directory)

**Step 3: Configure Audio Settings**
In the "Audio" section, select "Cisco Webex Audio" as the default audio type. You can also choose to allow participants to join via phone or VoIP.

**Step 4: Set Up Video Settings (Optional)**
If you want to enable video conferencing, click on the "Video" tab and select "Cisco Webex Video" as the default video type. You can also choose to allow participants to join via video.

**Step 5: Add Agenda and Notes (Optional)**
You can add an agenda and notes to the meeting invitation by clicking on the "Agenda" tab. This information will be visible to all invitees.

**Step 6: Send Invitations**
Click "Schedule" to send the meeting invitation to all invitees. The invitation will include a link to join the meeting, as well as dial-in information for audio-only participants.

**Step 7: Start the Meeting**
At the scheduled start time, click on the "Start" button to begin the conference call.
```

---

## Q4. What are the steps to create a backup of important files?

_in my docs: yes - took about 7.3s_

```
----- Retrieved chunks -----
Chunk 1:
**Creating a Backup of Important Files**

Backing up important files is a crucial step in protecting your data from loss or corruption. This article will guide you through the process of creating a backup of your important files.

**Step 1: Identify Important Files**

The first step in creating a backup is to identify the important files that need to be backed up. These may include documents, spre ...

Chunk 2:
d ensure that you have sufficient storage space.

**Step 4: Copy Your Files**

Copy your important files to your chosen backup device. Make sure to copy all the files and folders that you identified in Step 1.

**Step 5: Verify Your Backup**

Once you have copied your files, verify that they have been backed up successfully. Check the contents of your backup device to ensure that all files are pre ...

Chunk 3:
k.

**Additional Tips**

* **Backup Frequency**: Aim to backup your important files at least once a week, or more frequently if you work with sensitive or critical data.
* **Backup Location**: Store your backup device in a safe location, away from your computer and other electronic devices.
* **Versioning**: Consider using a backup software that supports versioning, which allows you to keep multip ...
---------------------------
```

**Answer:**
```
The steps to create a backup of important files are:

1.  **Identify Important Files**: Determine which files need backing up, such as documents, spreadsheets, and presentations, and make a list of the necessary files and folders.
2.  **Choose a Backup Method**: Select a method like using an External Hard Drive (by connecting it and copying files) or a Cloud Backup service.
3.  **Copy Your Files**: Copy all the files and folders identified in Step 1 to your chosen backup device.
4.  **Verify Your Backup**: Check the backup device's contents to confirm that all files are present and can be opened.
5.  **Schedule Regular Backups**: Set up your backup software to run automatically at a specified time, such as scheduling backups at least once a week.

Additional tips include storing the backup device in a safe location and considering backup software that supports versioning.
```

still notice the model skips over the real "Step 3" and "Step 6" from the doc and just renumbers its own list 1-5 — same chunking gap as before, chunk with "Step 3: Connect Your Backup Device" didnt make the top 3.

---

## Q5. What is the best way to train a neural network in PyTorch?

_in my docs: no - took about 0.5s (no llm call, hit the no-match rule)_

```
----- Retrieved chunks -----
Chunk 1:
**Resetting a Forgotten PIN**

If you have forgotten your PIN, you can reset it using the following steps:

**Step 1: Access the PIN Reset Tool**

1. Go to the company's intranet homepage and click on the "IT Support" link at the top right corner of the page.
2. Click on the "Self-Service" tab and then select "PIN Reset" from the drop-down menu.
3. You will be redirected to the PIN Reset Tool logi ...

Chunk 2:
nd download the VPN client software.
2. Run the installer and follow the prompts to install the software.
3. Once installed, launch the VPN client software.

**Step 2: Configure the VPN Connection**

1. In the VPN client software, click on "New Connection" and select "Company VPN" as the connection type.
2. Enter the company's VPN server address: `vpn.company.com`.
3. Enter your company login cred ...

Chunk 3:
**Configuring Email on an Android Device**

This article provides step-by-step instructions on how to configure email on an Android device. Please follow the steps below to set up your email account on your Android device.

**Prerequisites:**

* An Android device with a valid internet connection
* A valid email account (company email or personal email)
* Email account credentials (username and pas ...
---------------------------
```

**Answer:**
```
I could not find this in your documents.
```

this one didnt even call the llm, the no-match rule (config.py, distance above 0.75) catches it right away. thats why its half a second instead of 7-30s like the others.

---

## Summary

| # | Question | In docs? | Source | Grounded? |
|---|----------|----------|------------------|------------------|
| 1 | Configure VPN access for remote workers | yes | 003_Configuring_VPN_Access... | yes |
| 2 | Forgotten PIN | yes | 002_Resetting_a_Forgotten_PIN | yes |
| 3 | Cisco Webex conference call | yes | 005_Setting_Up_a_Conference_Call... | yes |
| 4 | Create a backup of important files | yes | 006_Creating_a_Backup... | yes, but skips "Step 3" |
| 5 | Train a neural network in PyTorch | no | unrelated chunks | yes, says it cant find it, no llm call |

Notes:
- for every real question it found the right doc, every time — retrieval
  doesnt change between runs
- Q4 still skips step 3 in the final answer, that chunk just isnt in the
  top 3 even though it exists somewhere in the store — same chunking gap
  as before
- Q5 shows the no-match rule working — doesnt even bother the llm, just
  answers straight away in under a second
