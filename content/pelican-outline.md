Title: Pelican: A Static Site Generator (SSG) Written In Python
Date: 2018-07-21
Category: Python
Summary: Notes for a presentation on static site generators and Pelican given to the Omaha Python User Group on 07/26/2018.
URL:
save_as: index.html

*Notes for a presentation on static site generators and Pelican given to the Omaha Python User Group on 07/26/2018.  This static site was rendered with pelican.*

## What Are SSGs?

Think of SSGs as a throwback to the old school with a modern twist: 

<img src="https://i.kinja-img.com/gawker-media/image/upload/s--dPeSSMpu--/18edh1z146cjapng.png" style="display:block; margin-left: auto; margin-right: auto;" height="350" width=350/>

Modern SSGs use markup languages and templating engines to produce HTML files.  Those HTML files, along with your static assets, are then uploaded onto a server where they are delivered to users.

[Full Stack Python](https://www.fullstackpython.com) is an example of a modern static site created with pelican.

## SSGS The Good And The Bad

Like any other technology there are pros and cons to using any framework and SSGs are no different.  Identifying a proper use case for SSGs revolves around this question:  

**How Much User Interaction Do I Require?**

The short answer: 

If you require user interaction beyond a contact form or comments you probably should consider a different tool.

### Pros:

 **1. Speed**

Served content is not dynamic.  A database is not queried to generate content.

**2. Security** 

Fewer attack vectors as your server is only delivering static content. 

**3. Easier Infrastructure Maintenance**

No multiple: servers, Operating Systems, dependencies, or database engines.

**4. Handles Traffic Spikes**

Uses a small amount of resources *see* [this post on Full Stack Python](https://www.fullstackpython.com/static-site-generator.html)

**5. Content Is Source Controlled**

Your content is not hidden in a database; it is part of your codebase.  Therefore, it can be subjected to pull requests and issues just like the rest of your code.

[Link to this site's repo.](https://github.com/Jeffallan/Pelican-With-Pelican)

### Cons

**1. No Realtime, Dynamic, Or Custom Content**

Altering content requires you to rerender your static HTML files.

Also, supporting multiple users, their likes, and preferences is best left to a framework that uses a database.

**2. Sparse User Interaction**

Depending on which SSG you chose there are some workarounds, plugins, and third party services for things like form submission, comments, and search.


**3. Not Every SSG Has An Admin Interface**

This is an important consideration if your content creation team is used to working out of a dashboard.

## Pelican from 10,000 Feet

**The Main Highlights Of Pelican Include: **

    - ReStructured Text and Markdown Support
    - Supports Articles and Pages Similar to WordPresss
    - Multiple Language Support
    - Code Highlighting
    - An Extensive Plugin and Theme Ecosystem
    - Templating with Jinja2
    - Atom and RSS Feeds
    - WordPress Import
    - Google Analytics Integration
    - Easy Deployment


## Why Chose Pelican To Update The Current Omaha Python User Group Website

We feel our current [website](http://www.omahapython.org) needs a needs a face lift.  This site is a WordPress site.

Pelican gives us the opportunity to migrate the old site's content with [ease](http://docs.getpelican.com/en/stable/importer.html) while both maintaining similar functionality and using Python to create the Omaha Python User Group's new website.

 


