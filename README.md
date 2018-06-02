# Character move

## Goal
I have a specific text I am trying to assure is encoded using the correct point locations in Unicode.

Evidence that I have a problem.

```
A kpö gɔɔ =plɛ naa: bhöpë nu ‘ö ‘wo “siʋ̈ ya mɛ kwi ‘gü, ‘ö ‘wo ‘nii da mɛ ‘gü
```

Sample text can be found here:

So now comes the interesting part.
https://github.com/silnrsi/wsresources/tree/master/scripts/Latn/mappings/sil-pua
### Attempted methodologies

I think that I am trying to target a character in SIL's PUA. I am led to this conclusion because David Rowe when looking at my data for another issue, mentioned that his version of the font CharisSIL showed the characters as inverted block. Suggesting that the PUA character had been moved to the main part of Unicode. I do not know which character was visible to him, as we were in a skype session.

My files are all in the directory `Character conversion test`
 I copied one word with the character to be converted to another text file, saved it in file `smalltext.txt `.  Then tried to use (UnicodeCCount)[http://scripts.sil.org/UnicodeCharacterCount] to tell me which characters are in the file.
results before
```


```

results after

 The only thing that happens when I run the file through techkit is that a BOM mark is added (at least according to UnicodeCCount). See file: `smalltext-post-teckit.txt `

**So, how do I correctly ID the character in question?**


### Included in this Repo

* SIL's Teckit PUA converter mapping files
* SIL's PUA Description Files
* Example test Files

### License and ownership

The content of this repo contains materials from SIL International. These materials are freely shared, but ownership belongs to SIL International. No additional licenses are granted or implied.

Language content for testing are excerpts of owned materials, used here under fair use.
