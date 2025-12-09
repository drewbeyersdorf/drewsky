import inquirer from 'inquirer';
import chalk from 'chalk';
import boxen from 'boxen';
import fs from 'fs-extra';

/**
 * Chain of Verification (CoVe) Command
 * Meta AI's 4-step verification process (23% hallucination reduction)
 *
 * Steps:
 * 1. Generate baseline response
 * 2. Plan verification questions
 * 3. Answer questions independently
 * 4. Generate final verified response
 */

export async function verifyCommand(options) {
  console.log(chalk.blue.bold('\n🔍 drewsky Chain of Verification (CoVe)\n'));
  console.log(chalk.dim('Meta AI methodology for 23% hallucination reduction\n'));

  // Check for workflow files
  const researchExists = await fs.pathExists('.research.md');
  const planExists = await fs.pathExists('.plan.md');

  if (!researchExists && !planExists && !options.file) {
    console.log(
      boxen(
        chalk.yellow.bold('⚠️  No Workflow Files Found') + '\n\n' +
        chalk.white('Create .research.md or .plan.md first, or specify a file:\n\n') +
        chalk.cyan('drewsky verify --file <path>'),
        {
          padding: 1,
          margin: 1,
          borderStyle: 'round',
          borderColor: 'yellow'
        }
      )
    );
    return;
  }

  // Determine which file to verify
  let fileToVerify = options.file;

  if (!fileToVerify) {
    const choices = [];
    if (researchExists) choices.push({ name: '.research.md', value: '.research.md' });
    if (planExists) choices.push({ name: '.plan.md', value: '.plan.md' });

    if (choices.length > 1) {
      const answer = await inquirer.prompt([
        {
          type: 'list',
          name: 'file',
          message: 'Which file do you want to verify?',
          choices
        }
      ]);
      fileToVerify = answer.file;
    } else {
      fileToVerify = choices[0].value;
    }
  }

  // Read the file
  let content;
  try {
    content = await fs.readFile(fileToVerify, 'utf8');
  } catch (error) {
    console.log(chalk.red(`\nError: Could not read ${fileToVerify}\n`));
    return;
  }

  console.log(chalk.white(`\nVerifying: ${chalk.cyan(fileToVerify)}\n`));

  // Extract claims from the file
  const claims = extractClaims(content);

  if (claims.length === 0) {
    console.log(
      boxen(
        chalk.yellow.bold('No Claims Found') + '\n\n' +
        chalk.white('Could not find any verifiable claims in this file.\n\n') +
        chalk.dim('Claims should have file:line references or specific assertions.'),
        {
          padding: 1,
          margin: 1,
          borderStyle: 'round',
          borderColor: 'yellow'
        }
      )
    );
    return;
  }

  console.log(chalk.white.bold(`Found ${claims.length} claim(s) to verify:\n`));

  // CoVe Process
  const verificationResults = [];

  for (let i = 0; i < claims.length; i++) {
    const claim = claims[i];
    console.log(chalk.cyan(`\n${i + 1}. ${claim.text}`));

    // Step 1: Show the baseline claim
    console.log(chalk.dim(`   Source: Line ${claim.line}`));

    // Step 2: Generate verification questions
    const questions = generateVerificationQuestions(claim);
    console.log(chalk.yellow('\n   Verification questions:'));
    questions.forEach((q, idx) => {
      console.log(chalk.dim(`   ${idx + 1}) ${q}`));
    });

    // Step 3: Prompt for manual verification
    const answer = await inquirer.prompt([
      {
        type: 'list',
        name: 'verified',
        message: '   Verification status:',
        choices: [
          { name: '✓ Verified - Claim is accurate', value: 'verified' },
          { name: '? Uncertain - Needs more investigation', value: 'uncertain' },
          { name: '✗ False - Claim is inaccurate', value: 'false' }
        ]
      }
    ]);

    let notes = '';
    if (answer.verified !== 'verified') {
      const notesAnswer = await inquirer.prompt([
        {
          type: 'input',
          name: 'notes',
          message: '   Notes (optional):'
        }
      ]);
      notes = notesAnswer.notes;
    }

    verificationResults.push({
      claim: claim.text,
      line: claim.line,
      status: answer.verified,
      notes,
      questions
    });
  }

  // Step 4: Display final verification report
  console.log(chalk.blue.bold('\n\n📋 Verification Report\n'));

  const verified = verificationResults.filter(r => r.status === 'verified').length;
  const uncertain = verificationResults.filter(r => r.status === 'uncertain').length;
  const false_ = verificationResults.filter(r => r.status === 'false').length;

  console.log(chalk.green(`✓ Verified: ${verified}`));
  console.log(chalk.yellow(`? Uncertain: ${uncertain}`));
  console.log(chalk.red(`✗ False: ${false_}\n`));

  // Show issues
  const issues = verificationResults.filter(r => r.status !== 'verified');
  if (issues.length > 0) {
    console.log(chalk.yellow.bold('Issues Found:\n'));
    issues.forEach((issue, idx) => {
      const icon = issue.status === 'false' ? chalk.red('✗') : chalk.yellow('?');
      console.log(`${icon} ${chalk.white(issue.claim)}`);
      console.log(chalk.dim(`  Line ${issue.line}`));
      if (issue.notes) {
        console.log(chalk.dim(`  Notes: ${issue.notes}`));
      }
      console.log('');
    });
  }

  // Generate verification summary file
  const summary = generateVerificationSummary(fileToVerify, verificationResults);
  const summaryFile = `.verification-${Date.now()}.md`;

  await fs.writeFile(summaryFile, summary);

  console.log(
    boxen(
      chalk.green.bold('Verification Complete') + '\n\n' +
      chalk.white(`Report saved: ${chalk.cyan(summaryFile)}\n\n`) +
      chalk.white(`Verified: ${chalk.green(verified)}/${verificationResults.length}\n`) +
      (issues.length > 0
        ? chalk.yellow(`\n⚠️  ${issues.length} claim(s) need attention`)
        : chalk.green('✓ All claims verified')),
      {
        padding: 1,
        margin: 1,
        borderStyle: 'round',
        borderColor: verified === verificationResults.length ? 'green' : 'yellow'
      }
    )
  );

  console.log(chalk.dim('\nFor more on CoVe: https://arxiv.org/abs/2309.11495\n'));
}

function extractClaims(content) {
  const claims = [];
  const lines = content.split('\n');

  lines.forEach((line, index) => {
    // Look for lines with file:line references (verified claims)
    if (line.includes(':') && /\d+/.test(line) && (line.includes('✓') || line.includes('src/') || line.includes('lib/'))) {
      claims.push({
        text: line.replace(/^[\s\-✓\*]+/, '').trim(),
        line: index + 1,
        type: 'file-reference'
      });
    }
    // Look for confidence percentages
    else if (line.includes('Confidence:') && line.includes('%')) {
      claims.push({
        text: line.trim(),
        line: index + 1,
        type: 'confidence'
      });
    }
    // Look for facts/assumptions
    else if ((line.includes('- ✓') || line.includes('- ?')) && line.length > 10) {
      claims.push({
        text: line.replace(/^[\s\-✓\?]+/, '').trim(),
        line: index + 1,
        type: 'assertion'
      });
    }
  });

  return claims;
}

function generateVerificationQuestions(claim) {
  const questions = [];

  if (claim.type === 'file-reference') {
    questions.push('Does the referenced file exist at the specified location?');
    questions.push('Does the code at that line match the claim?');
    questions.push('Has the file been modified since this claim was made?');
  } else if (claim.type === 'confidence') {
    questions.push('What evidence supports this confidence level?');
    questions.push('Are there any risk factors that could lower confidence?');
    questions.push('Have similar tasks been completed successfully before?');
  } else if (claim.type === 'assertion') {
    questions.push('What evidence supports this assertion?');
    questions.push('Are there any contradicting sources?');
    questions.push('Has this been independently verified?');
  }

  return questions;
}

function generateVerificationSummary(filename, results) {
  const date = new Date().toLocaleString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });

  let summary = `# Verification Report: ${filename}

**Date**: ${date}
**Method**: Chain of Verification (CoVe)

---

## Summary

**Total claims**: ${results.length}
**Verified**: ${results.filter(r => r.status === 'verified').length}
**Uncertain**: ${results.filter(r => r.status === 'uncertain').length}
**False**: ${results.filter(r => r.status === 'false').length}

---

## Detailed Results

`;

  results.forEach((result, index) => {
    const icon = result.status === 'verified' ? '✓' : result.status === 'false' ? '✗' : '?';
    summary += `### ${index + 1}. ${icon} ${result.claim}

**Line**: ${result.line}
**Status**: ${result.status}
${result.notes ? `**Notes**: ${result.notes}\n` : ''}
**Verification Questions**:
${result.questions.map((q, i) => `${i + 1}. ${q}`).join('\n')}

---

`;
  });

  summary += `
## Recommendations

`;

  const issues = results.filter(r => r.status !== 'verified');
  if (issues.length > 0) {
    summary += `⚠️  ${issues.length} claim(s) need attention:

`;
    issues.forEach(issue => {
      summary += `- [ ] Review: ${issue.claim} (Line ${issue.line})\n`;
    });
  } else {
    summary += `✓ All claims verified successfully. No action needed.\n`;
  }

  summary += `
---

**Generated by drewsky CLI** | [CoVe Research](https://arxiv.org/abs/2309.11495)
`;

  return summary;
}
