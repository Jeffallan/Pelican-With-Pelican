Title: Pelican: A Static Site Generator (SSG) Written In Python
Date: 2018-07-21
Category: Python

## What Are SSGs?

Think of SSGs as a throwback to the old school with a modern twist: 

![geocities website](https://i.kinja-img.com/gawker-media/image/upload/s--dPeSSMpu--/18edh1z146cjapng.png)

Modern SSGs use markup languages and templating engines to produce HTML files.  Those HTML files, along with your static assets, are then uploaded onto a server where they are served.

[Full Stack Python](https://www.fullstackpython.com) is an example of a modern static site created with pelican.

## SSGS The Good And The Bad

Like any other technology there are pros and cons to using any framework and SSGS are no different.  Identifying a proper use case for SSGS revolves around this question.  

**How Much Interaction Do I Need With A Server?**

The short answer: 

If you require user interaction beyond a contact form or comments you probably should consider a different tool.

### Pros:

 **1. Speed**

No querying a database to generate content.

**2. Security** 

Less attack vectors.

**3. Easier Infrastructure Maintenance**

No multiple: servers, OSes, dependencies, or DB engines.

**4. Handles Traffic Spikes**

Uses a small amount of resources *see* [this post on Full Stack Python](https://www.fullstackpython.com/static-site-generator.html)

**5. Content Is Source Controlled**

Your content is part of the codebase.  Therefore, it can be subjected to pull requests and issues just like the rest of your code.

### Cons

**1. No Realtime, Dynamic, Or Custom Content**

Altering content requires you to rerender your static HTML files.

Also, supporting multiple users, their likes, and preferences is best left to a framework that uses a server.

**2. No User Input Per Se**

Depending on which SSG you chose there are some workarounds, plugins, and third party services for things like form submission, comments, and search.


**3. Not Every SSG Has An Admin Interface**

This is an important consideration if your content creation team is used to working out of a dashboard.

## Why The We Chose Pelican

## Pelican from 10,000 Feet 

## Resources 

### Repositories
[GitHub Repo](https://github.com/getpelican/pelican)
[Themes](https://github.com/getpelican/pelican-themes)
[Plugins(https://github.com/getpelican/pelican-plugins)]

### Documentation

[Pelican Docs](http://docs.getpelican.com/en/stable/)

### Third Party Sites

[Pelican-Specific Links From Full Stack Python](https://www.fullstackpython.com/pelican.html)
[General Static Site Generator Links From Full Stack Python](https://www.fullstackpython.com/static-site-generator.html)

	


