import inquirer from 'inquirer';
import chalk from 'chalk';
import ora from 'ora';
import boxen from 'boxen';
import fs from 'fs-extra';
import path from 'path';
import { updateMetrics } from '../utils/file-helpers.js';

export async function planCommand(options) {
  console.log(chalk.blue.bold('\n📋 drewsky Plan Generator\n'));

  let researchData = null;
  let taskName = '';

  // Check if .research.md exists
  const researchExists = await fs.pathExists('.research.md');

  if (researchExists && options.fromResearch) {
    const spinner = ora('Reading existing research...').start();
    try {
      const researchContent = await fs.readFile('.research.md', 'utf8');
      // Extract task name from research file
      const taskMatch = researchContent.match(/# Research: (.+)/);
      if (taskMatch) {
        taskName = taskMatch[1];
      }
      spinner.succeed('Research loaded');
      researchData = researchContent;
    } catch (error) {
      spinner.fail('Could not read research file');
    }
  }

  // Prompt for task name if not from research
  if (!taskName) {
    const taskAnswer = await inquirer.prompt([
      {
        type: 'input',
        name: 'task',
        message: chalk.cyan('Task:') + ' What are you implementing?',
        validate: (input) => input.length > 0 || 'Task name is required'
      }
    ]);
    taskName = taskAnswer.task;
  }

  console.log(chalk.yellow('\n📊 TASK LEDGER (Strategic)\n'));

  // Collect facts
  const facts = [];
  let addingFacts = true;
  while (addingFacts) {
    const factAnswer = await inquirer.prompt([
      {
        type: 'input',
        name: 'fact',
        message: chalk.green('✓ Verified Fact:') + ' (with file:line reference, or press Enter to skip)',
      }
    ]);

    if (factAnswer.fact.trim()) {
      facts.push(factAnswer.fact.trim());
    } else {
      addingFacts = false;
    }
  }

  // Collect guesses/assumptions
  const guesses = [];
  let addingGuesses = true;
  while (addingGuesses) {
    const guessAnswer = await inquirer.prompt([
      {
        type: 'input',
        name: 'guess',
        message: chalk.yellow('? Assumption:') + ' (needs validation, or press Enter to skip)',
      }
    ]);

    if (guessAnswer.guess.trim()) {
      guesses.push(guessAnswer.guess.trim());
    } else {
      addingGuesses = false;
    }
  }

  // Collect decision points
  const decisions = [];
  let addingDecisions = true;
  while (addingDecisions) {
    const decisionAnswer = await inquirer.prompt([
      {
        type: 'input',
        name: 'decision',
        message: chalk.magenta('[ ] Decision Point:') + ' (architecture choice, or press Enter to skip)',
      }
    ]);

    if (decisionAnswer.decision.trim()) {
      decisions.push(decisionAnswer.decision.trim());
    } else {
      addingDecisions = false;
    }
  }

  console.log(chalk.yellow('\n⚙️  PROGRESS LEDGER (Tactical)\n'));
  console.log(chalk.dim('Add atomic MAKER steps (<30 min each)\n'));

  // Collect steps
  const steps = [];
  let addingSteps = true;
  let stepNumber = 1;

  while (addingSteps) {
    console.log(chalk.blue(`\nStep ${stepNumber}:`));

    const stepAnswers = await inquirer.prompt([
      {
        type: 'input',
        name: 'name',
        message: 'Step name:',
        validate: (input) => {
          if (stepNumber === 1 && !input.trim()) {
            return 'At least one step is required';
          }
          return true;
        }
      }
    ]);

    if (!stepAnswers.name.trim()) {
      addingSteps = false;
      continue;
    }

    const stepDetails = await inquirer.prompt([
      {
        type: 'input',
        name: 'input',
        message: '  Input:',
        default: stepNumber === 1 ? 'Current codebase' : `Output from Step ${stepNumber - 1}`
      },
      {
        type: 'input',
        name: 'action',
        message: '  Action:',
        validate: (input) => input.length > 0 || 'Action is required'
      },
      {
        type: 'input',
        name: 'output',
        message: '  Output:',
        validate: (input) => input.length > 0 || 'Output is required'
      },
      {
        type: 'input',
        name: 'verification',
        message: '  Verification:',
        default: 'Manual review'
      },
      {
        type: 'number',
        name: 'confidence',
        message: '  Confidence (0-100):',
        default: 80,
        validate: (input) => (input >= 0 && input <= 100) || 'Must be between 0-100'
      },
      {
        type: 'number',
        name: 'time',
        message: '  Time estimate (minutes):',
        default: 15,
        validate: (input) => input > 0 || 'Must be positive'
      }
    ]);

    steps.push({
      number: stepNumber,
      name: stepAnswers.name.trim(),
      ...stepDetails
    });

    stepNumber++;
  }

  // Calculate totals
  const totalSteps = steps.length;
  const totalTime = steps.reduce((sum, step) => sum + step.time, 0);
  const avgConfidence = Math.round(
    steps.reduce((sum, step) => sum + step.confidence, 0) / totalSteps
  );

  // Generate plan document
  const date = new Date().toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });

  let planDoc = `# Implementation Plan: ${taskName}

**Created**: ${date}
**Status**: Draft

---

## Task Ledger (Strategic)

### Facts (Verified)
`;

  if (facts.length > 0) {
    facts.forEach(fact => {
      planDoc += `- ✓ ${fact}\n`;
    });
  } else {
    planDoc += `- *(No facts recorded)*\n`;
  }

  planDoc += `\n### Guesses (Need Validation)\n`;

  if (guesses.length > 0) {
    guesses.forEach(guess => {
      planDoc += `- ? ${guess}\n`;
    });
  } else {
    planDoc += `- *(No assumptions recorded)*\n`;
  }

  planDoc += `\n### Decision Points\n`;

  if (decisions.length > 0) {
    decisions.forEach(decision => {
      planDoc += `- [ ] ${decision}\n`;
    });
  } else {
    planDoc += `- *(No decision points recorded)*\n`;
  }

  planDoc += `\n---

## Progress Ledger (Tactical)

`;

  steps.forEach(step => {
    planDoc += `### Step ${step.number}: ${step.name}
- **Input**: ${step.input}
- **Action**: ${step.action}
- **Output**: ${step.output}
- **Verification**: ${step.verification}
- **Confidence**: ${step.confidence}%
- **Time**: ${step.time} minutes

`;
  });

  planDoc += `---

## Test Commands

\`\`\`bash
# Step verification commands
${steps.map((step, idx) => `# Step ${idx + 1}: ${step.verification}`).join('\n')}

# Final verification
# (Add your test command here)
\`\`\`

---

## Overall Assessment

**Total Steps**: ${totalSteps}
**Estimated Time**: ${totalTime} minutes (${Math.round(totalTime / 60 * 10) / 10} hours)
**Overall Confidence**: ${avgConfidence}%

---

## Approval

- [ ] Plan reviewed
- [ ] Steps are atomic (<30 min each)
- [ ] Test commands defined
- [ ] Ready to implement

---

**Generated by drewsky CLI** | [Documentation](https://github.com/drewbeyersdorf/agent-improvement-techniques)
`;

  // Write plan file
  const spinner = ora('Generating plan...').start();

  try {
    await fs.writeFile('.plan.md', planDoc);
    await updateMetrics({ plansCreated: 1 });
    spinner.succeed('Plan created successfully');

    console.log(
      boxen(
        chalk.green.bold('✓ Plan Generated') + '\n\n' +
        chalk.white(`File: ${chalk.cyan('.plan.md')}\n`) +
        chalk.white(`Steps: ${chalk.yellow(totalSteps)}\n`) +
        chalk.white(`Time: ${chalk.yellow(totalTime)} minutes\n`) +
        chalk.white(`Confidence: ${chalk.yellow(avgConfidence)}%\n\n`) +
        chalk.dim('Review the plan and get approval before implementing.'),
        {
          padding: 1,
          margin: 1,
          borderStyle: 'round',
          borderColor: 'green'
        }
      )
    );

    console.log(chalk.blue('\n📌 Next Steps:'));
    console.log(chalk.white('  1. Review .plan.md'));
    console.log(chalk.white('  2. Get stakeholder approval'));
    console.log(chalk.white('  3. Begin implementation'));
    console.log(chalk.white('  4. Use drewsky status to track progress\n'));

  } catch (error) {
    spinner.fail('Failed to create plan');
    console.error(chalk.red(error.message));
    process.exit(1);
  }
}
