# Introduction

This is the source code for a presentation I gave to the Omaha Python User Group on 07/26/2018 concerning static site generators and Pelican: a static site generator written for python.

## Quick Deploy instructions for Github Project Pages

I deployed this static site from the /docs folder of my master branch.

In doing so I encountered a small snag as my first few attempts to deploy this site rendered without any CSS styling.

Assuming you ran pelican-quickstart there should be a file called publishconf.py.  These are your production settings.

Be sure to edit the site url setting as follows: SITEURL = 'https://<username>.github.io/<repo name>'

Also set relative urls to true: RELATIVE_URLS = True.  For an explination see this [issue](https://github.com/getpelican/pelican/issues/1526)

To deploy a production build run: 

```bash
pelican content -o `pwd`/docs -s publishconf.py
```

This command generates your static content in your /docs folder using your production settings.

Then add, commit, and push those changes to your master branch.
