# Data Downloading and Processing

While the FFHQ-256 dataset has been uploaded to our Azure Blob Storage account already, whenever we want to train a model, etc., we need to download the data from the cloud storage to local machines, and we also need to extract the images from that file.

## Step 1: Download `azcopy`

First, download the `azcopy` program from Azure. For most Linux distributions (including SUN Lab computers and Vast.AI/Lambda instances), the following link should work: <https://aka.ms/downloadazcopy-v10-linux>.

*Task 1:*

*Without physically going to the SUN Lab, figure out a way to download this file onto your home directory (the tilde `~`, remember?) on SUN Lab computers.*

## Step 2: Unpack the zipped file.

Verify that the downloaded file has ending suffix `.tar.gz`. Navigate to the directory (the `cd` command) where the file is located. Run the following command, replacing the bracketed portion with the full name of the downloaded file.
```
tar xf [FILE_NAME]
```

## Step 3: Check If Installation Is Correct

The command above should extract a new directory in the current directory. (Check with the `ls` command.) Go into the directory, and check that there is a file named `azcopy`. It should be directly executable; run with the following command:
<pre>
./azcopy
</pre>
The "`./`" is necessary. The reason is kind of boring: when a command begins with a word, the program will try to interpret this as a command. Without the "`./`," we would get a "command not found" error.

If everything was right, you should see the terminal printing a bunch of manual information.

## Step 4: Download the FFHQ Dataset

*Task 2:*

*Find you shared access token for the container named "`container`" in our Azure Blob Storage account. You'll need to find it by first navigating in the Azure portal to the container.*

If you have previously saved your shared access token, that works too, so long as it hasn't expired. (If it did, then you'll know when there's an error later.)

Your SAS (Shared Access Token) URL should look something like:
<pre>
https://<...>.blob.core.windows.net/container?sp=<...>&st=<...>&se=<...>&sv=<...>&sr=<...>&sig=<...>
</pre>

There's one thing about how URLs work: when you want to pass additional information when you are sending a request (e.g., requesting to download the file), you put the additional information after a `?`, which follows the link. If there're multiple parameters to pass in, they should be separated by `&`.

So really, the link part ends at `<...>/container`.

Anyways, first, try and list the directory by the following command:
<pre>
./azcopy ls [SAS_URL_FOR_CONTAINER]
</pre>
Expect A LOT of output. If helpful, use commands you know/google to weed out information you don't need. Of course, you could simply go to the Azure portal and browse the cloud storage.

Now, to refer to the `ffhq-r08.tfrecord` inside the `container` container, use the following URL:
<pre>
https://<...>.blob.core.windows.net/container/<u>ffhq-r08.tfrecords</u>?sp=<...>&st=<...>&se=<...>&sv=<...>&sr=<...>&sig=<...>
</pre>
See how the file name `ffhq-r08.tfrecords` goes right before the `?` and after another `/` representing inside the `container` the directory?

So, to copy that to the machine you're working with (or your *computing server*), run
<pre>
./azcopy cp https://<...>.blob.core.windows.net/container/ffhq-r08.tfrecords?sp=<...>&st=<...>&se=<...>&sv=<...>&sr=<...>&sig=<...> .
</pre>
Don't forget the `.` at the end! Remember, the single dot represents the current directory: we're copying the file that the URL represents **to the current directory**.

## Step 5: Examining the file

Now, when you run `ls -la`, you should see that the file has been successfully downloaded. How do you <u>verify the integrity</u> (i.e., check that you've downloaded the file correctly) of the file? There is something known as the MD5 hash. 

*Task 3:*

*Find out a way to obtain the MD5 hash of the downloaded file. Then, go to <https://github.com/NVlabs/ffhq-dataset/blob/master/download_ffhq.py> and find the correct MD5 hash for the file. Compare to make sure that your download is correct.*

## Step 6: Extracting the dataset

Download ``extract_ffhq.py``. 

*Task 4:*

*Try and run the code. There will be errors. Try and fix them accordingly. If there is a missing package, find out what is missing and how to install it. If some path (i.e., the string that locates a file/directory, such as `/home/daa5724/abc.txt`) does not exist, you may need to create an empty directory with that name manually (which command is that?).*

## Step 7: Check Some Images (Optional)

Find out a way to open some of the images. Are they open-able? Do they look okay?