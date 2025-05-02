---
title: 'Apache Tika'
metadata:
    description: 'Menu Editor'
    author: 'Eleni Kullira'
content:
    items:
        - '@self.children'
    limit: 5
    order:
        by: date
        dir: desc
    pagination: true
    url_taxonomy_filters: true
taxonomy:
    category:
        - adminmanual
    tag:
        - howto
---

![Tika](tikalogo.PNG?classes=minsize) 

## TIKA DOCUMENTATION

[Apache Tika](https://tika.apache.org/) is a library used for document type detection and content extraction from various file formats. The Apache Tika™ toolkit detects and extracts metadata and text from over a thousand different file types (such as PPT, XLS, and PDF). All of these file types can be parsed through a single interface, making Tika useful for search engine indexing, content analysis, translation, and much more. 
Internally, Tika uses existing various document parsers and document type detection techniques to detect and extract data.Using Tika, one can develop a universal type detector and content extractor to extract both structured text as well as metadata from different types of documents such as spreadsheets, text documents, images, PDFs and even multimedia input formats to a certain extent.

According to filext.com, there are about 15k to 51k content types, and this number is growing day by day. Data is being stored in various formats such as text documents, excel spreadsheet, PDFs, images, and multimedia files, to name a few. Therefore, applications such as search engines and content management systems need additional support for easy extraction of data from these document types. Apache Tika serves this purpose by providing a generic API to locate and extract data from multiple file formats.

**Various applications use Apache Tika. Here we will discuss step by step the use of Tika in coreBOS.**

Firstly you need to install and run Apache Tika. The easiest way to do this is using docker.

```
docker run -d -p 9998:9998 apache/tika:latest
```

Activate Read Documents Content - ApacheTika cron.

![coreBOS-Tika Cron](cron.png?classes=maxsize)

Create the Global Variable (`Apache_Tika_URL`) where you set the URL where Tika is running (the IP of the docker container which you can obtain with `docker inspect`)

![Apache_Tika_URL](globalvariable.PNG?classes=maxsize)

After the first three steps, the Apache Tika is setup and ready to work. The cron will go through all the document records and index the attached file. After that it will index all the new and modified files.

### Testing Apache Tika

In the Documents module, upload several documents that you will use for tests. Wait for the cron to run or launch it manually.

In the Documents module, you will see the "Search Documents" button, you can write the word or the phrase you want to find and you can search the files' contents.

![Searchdoc](searchdoc.png?classes=maxsize)

You can use also use the Global Search for a full-text search into files.

![Search](search.png?classes=maxsize)

<head>
  <style type="text/css">
  .minsize {
  width: 200px ;
 }
.maxsize {
  width: 600px ;
 }
  </style>
</head>