import fetch from 'node-fetch';
import path from 'node:path';
import fs from 'node:fs/promises';

/**
 *
 * @param {number} amount
 * @returns {string}
 */
function whiteSpaces(amount) {
  let spaces = [];
  for (let i = 0; i < amount; i++) spaces.push(' ');
  return spaces.join('');
}

const downloadUrl = await fetch(
  'https://download.mozilla.org/download/en-US/?product=firefox-devedition-latest-ssl&os=linux64&lang=en-US',
  {
    compress: true,
    redirect: 'manual',
  },
).then((res) => res.headers.get('location'));
if (!downloadUrl) throw new Error('Failed to fetch download URL');

const version = path.parse(downloadUrl).name.split('-')[1].slice(0, -4);

const specFile = await fs.readFile('../firefox-developer-edition.spec', 'utf8');

/**
 *
 * @param {string} content
 * @param {string} version
 */
function specUpdater(content, version) {
  if (!content || !version) throw new Error('Invalid content or version');
  const lines = content.split('\n');
  const versionIndex = lines.findIndex((val) => val.startsWith('Version:'));
  if (versionIndex < 0) throw new Error('Failed to parse current version');
  lines[versionIndex] = `Version:${whiteSpaces(12)}${version}`;
  return lines.join('\n');
}

await fs.writeFile(
  '../firefox-developer-edition.spec',
  specUpdater(specFile, version),
);
